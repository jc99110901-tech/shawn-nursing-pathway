#!/usr/bin/env python3

import argparse
import json
from pathlib import Path

from reportlab.graphics import renderPDF
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "docs" / "SNP-Skill-1分钟上手指南.pdf"

REPO_URL = "https://github.com/jc99110901-tech/shawn-nursing-pathway"
LITE_URL = (
    "https://raw.githubusercontent.com/jc99110901-tech/"
    "shawn-nursing-pathway/main/dist/shawn-nursing-pathway-lite.md"
)
FULL_URL = (
    "https://raw.githubusercontent.com/jc99110901-tech/"
    "shawn-nursing-pathway/main/dist/shawn-nursing-pathway-full.md"
)
WORKBUDDY_URL = (
    "https://raw.githubusercontent.com/jc99110901-tech/"
    "shawn-nursing-pathway/main/dist/shawn-nursing-pathway-workbuddy.zip"
)
SUITE_URL = (
    "https://raw.githubusercontent.com/jc99110901-tech/"
    "shawn-nursing-pathway/main/dist/shawn-nursing-pathway-suite.zip"
)

INK = HexColor("#18302E")
TEAL = HexColor("#177A70")
TEAL_DARK = HexColor("#0E5F58")
TEAL_PALE = HexColor("#E6F2EF")
CORAL = HexColor("#E45F4B")
CORAL_PALE = HexColor("#FBEAE6")
YELLOW = HexColor("#F1C84B")
YELLOW_PALE = HexColor("#FFF7D6")
BLUE = HexColor("#287AA8")
BLUE_PALE = HexColor("#E9F3F8")
GRAY = HexColor("#65716E")
LIGHT_GRAY = HexColor("#F4F6F5")
MID_GRAY = HexColor("#D9E0DE")
WHITE = white

PAGE_W, PAGE_H = A4
MARGIN = 44


def register_fonts():
    candidates = [
        (
            "/System/Library/Fonts/STHeiti Light.ttc",
            "/System/Library/Fonts/STHeiti Medium.ttc",
        ),
        (
            str(Path.home() / "Library/Fonts/NotoSansCJKsc-Medium.otf"),
            str(Path.home() / "Library/Fonts/NotoSansCJKsc-Medium.otf"),
        ),
    ]
    for regular_path, bold_path in candidates:
        if Path(regular_path).exists() and Path(bold_path).exists():
            try:
                regular_args = {"subfontIndex": 0} if regular_path.endswith(".ttc") else {}
                bold_args = {"subfontIndex": 0} if bold_path.endswith(".ttc") else {}
                pdfmetrics.registerFont(
                    TTFont("SNPRegular", regular_path, **regular_args)
                )
                pdfmetrics.registerFont(TTFont("SNPBold", bold_path, **bold_args))
                return "SNPRegular", "SNPBold"
            except Exception:
                continue

    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
    return "STSong-Light", "STSong-Light"


REGULAR, BOLD = register_fonts()


def normalize_text(text):
    return " ".join(text.strip().split())


def wrap_text(text, font_name, font_size, max_width):
    text = normalize_text(text)
    lines = []
    current = ""
    for char in text:
        candidate = current + char
        if current and pdfmetrics.stringWidth(
            candidate, font_name, font_size
        ) > max_width:
            lines.append(current.rstrip())
            current = char.lstrip()
        else:
            current = candidate
    if current:
        lines.append(current.rstrip())
    return lines


def draw_wrapped(
    c,
    text,
    x,
    y,
    width,
    font_name=REGULAR,
    font_size=12,
    leading=18,
    color=INK,
    max_lines=None,
):
    lines = wrap_text(text, font_name, font_size, width)
    if max_lines is not None:
        lines = lines[:max_lines]
    c.setFillColor(color)
    c.setFont(font_name, font_size)
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def draw_label(c, text, x, y, fill, text_color=WHITE, width=None):
    pad_x = 10
    h = 24
    if width is None:
        width = pdfmetrics.stringWidth(text, BOLD, 10) + pad_x * 2
    c.setFillColor(fill)
    c.roundRect(x, y - h + 5, width, h, 5, fill=1, stroke=0)
    c.setFillColor(text_color)
    c.setFont(BOLD, 10)
    c.drawCentredString(x + width / 2, y - 11, text)


def draw_header(c, section, page_num, version):
    c.setFillColor(INK)
    c.setFont(BOLD, 10)
    c.drawString(MARGIN, PAGE_H - 33, "SNP Skill")
    c.setFillColor(GRAY)
    c.setFont(REGULAR, 9)
    c.drawRightString(PAGE_W - MARGIN, PAGE_H - 33, section)
    c.setStrokeColor(MID_GRAY)
    c.setLineWidth(0.8)
    c.line(MARGIN, PAGE_H - 45, PAGE_W - MARGIN, PAGE_H - 45)
    draw_footer(c, page_num, version)


def draw_footer(c, page_num, version):
    c.setStrokeColor(MID_GRAY)
    c.setLineWidth(0.7)
    c.line(MARGIN, 39, PAGE_W - MARGIN, 39)
    c.setFillColor(GRAY)
    c.setFont(REGULAR, 8.5)
    c.drawString(MARGIN, 24, f"SNP Skill {version}  |  中文优先")
    c.drawRightString(PAGE_W - MARGIN, 24, f"{page_num} / 5")


def draw_title(c, eyebrow, title, subtitle, y=744):
    c.setFillColor(CORAL)
    c.setFont(BOLD, 10)
    c.drawString(MARGIN, y, eyebrow)
    y -= 43
    c.setFillColor(INK)
    c.setFont(BOLD, 28)
    c.drawString(MARGIN, y, title)
    y -= 31
    c.setFillColor(GRAY)
    c.setFont(REGULAR, 12)
    c.drawString(MARGIN, y, subtitle)
    return y - 26


def draw_qr(c, url, x, y, size):
    c.setFillColor(WHITE)
    c.roundRect(x - 6, y - 6, size + 12, size + 12, 5, fill=1, stroke=0)
    widget = qr.QrCodeWidget(url)
    x1, y1, x2, y2 = widget.getBounds()
    width = x2 - x1
    height = y2 - y1
    drawing = Drawing(
        size,
        size,
        transform=[size / width, 0, 0, size / height, 0, 0],
    )
    drawing.add(widget)
    renderPDF.draw(drawing, c, x, y)
    c.linkURL(url, (x, y, x + size, y + size), relative=0)


def draw_link(c, label, url, x, y, font_size=10.5, color=BLUE):
    c.setFillColor(color)
    c.setFont(BOLD, font_size)
    c.drawString(x, y, label)
    width = pdfmetrics.stringWidth(label, BOLD, font_size)
    c.setStrokeColor(color)
    c.setLineWidth(0.6)
    c.line(x, y - 2, x + width, y - 2)
    c.linkURL(url, (x, y - 4, x + width, y + font_size + 2), relative=0)
    return width


def draw_step(c, number, title, body, y, accent=TEAL):
    circle_x = MARGIN + 21
    c.setFillColor(accent)
    c.circle(circle_x, y - 2, 19, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont(BOLD, 15)
    c.drawCentredString(circle_x, y - 7, str(number))
    c.setFillColor(INK)
    c.setFont(BOLD, 14)
    c.drawString(MARGIN + 54, y + 4, title)
    draw_wrapped(
        c,
        body,
        MARGIN + 54,
        y - 18,
        PAGE_W - MARGIN * 2 - 54,
        font_size=11,
        leading=16,
        color=GRAY,
        max_lines=2,
    )


def draw_card(
    c,
    x,
    y,
    width,
    height,
    title,
    body,
    fill=LIGHT_GRAY,
    accent=TEAL,
    title_size=13,
    body_size=10.5,
    body_leading=15,
    url=None,
):
    c.setFillColor(fill)
    c.roundRect(x, y - height, width, height, 7, fill=1, stroke=0)
    c.setFillColor(accent)
    c.roundRect(x, y - height, 6, height, 3, fill=1, stroke=0)
    c.setFillColor(INK)
    c.setFont(BOLD, title_size)
    c.drawString(x + 18, y - 25, title)
    draw_wrapped(
        c,
        body,
        x + 18,
        y - 49,
        width - 36,
        font_size=body_size,
        leading=body_leading,
        color=GRAY,
    )
    if url:
        c.linkURL(url, (x, y - height, x + width, y), relative=0)


def page_cover(c, version):
    c.setFillColor(TEAL_DARK)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(YELLOW)
    c.rect(0, PAGE_H - 18, PAGE_W, 18, fill=1, stroke=0)

    c.setFillColor(WHITE)
    c.setFont(BOLD, 12)
    c.drawString(MARGIN, PAGE_H - 70, "Shawn说护理")
    draw_label(c, f"公开版 {version}", PAGE_W - MARGIN - 86, PAGE_H - 55, CORAL, width=86)

    c.setFillColor(WHITE)
    c.setFont(BOLD, 35)
    c.drawString(MARGIN, PAGE_H - 155, "SNP Skill")
    c.setFont(BOLD, 31)
    c.drawString(MARGIN, PAGE_H - 199, "1 分钟上手指南")

    c.setFillColor(YELLOW_PALE)
    c.setFont(REGULAR, 15)
    c.drawString(MARGIN, PAGE_H - 237, "不会 Skill、Prompt、知识库，也能用")

    box_y = PAGE_H - 292
    box_h = 100
    c.setFillColor(WHITE)
    c.roundRect(MARGIN, box_y - box_h, PAGE_W - MARGIN * 2, box_h, 8, fill=1, stroke=0)
    c.setFillColor(CORAL)
    c.setFont(BOLD, 11)
    c.drawString(MARGIN + 20, box_y - 25, "最简单的用法")
    c.setFillColor(INK)
    c.setFont(BOLD, 18)
    c.drawString(MARGIN + 20, box_y - 55, "下载 Lite → 上传 AI → 直接提问")
    c.setFillColor(GRAY)
    c.setFont(REGULAR, 10.5)
    c.drawString(MARGIN + 20, box_y - 78, "手机、电脑、普通 AI 对话都从这条路开始。")

    step_y = 390
    for number, title, body in [
        ("1", "下载", "点开 Lite 中文单文件"),
        ("2", "上传", "放进一个新的 AI 对话"),
        ("3", "提问", "说出你现在最真实的问题"),
    ]:
        c.setFillColor(YELLOW if number != "2" else CORAL)
        c.circle(MARGIN + 20, step_y, 17, fill=1, stroke=0)
        c.setFillColor(INK if number != "2" else WHITE)
        c.setFont(BOLD, 13)
        c.drawCentredString(MARGIN + 20, step_y - 5, number)
        c.setFillColor(WHITE)
        c.setFont(BOLD, 13)
        c.drawString(MARGIN + 50, step_y + 3, title)
        c.setFillColor(TEAL_PALE)
        c.setFont(REGULAR, 10.5)
        c.drawString(MARGIN + 50, step_y - 16, body)
        step_y -= 66

    draw_qr(c, REPO_URL, PAGE_W - MARGIN - 96, 80, 96)
    c.setFillColor(WHITE)
    c.setFont(BOLD, 9.5)
    c.drawString(PAGE_W - MARGIN - 96, 66, "扫码打开 GitHub")
    draw_link(
        c,
        "点这里下载 Lite 中文单文件",
        LITE_URL,
        MARGIN,
        143,
        11,
        YELLOW,
    )
    draw_link(
        c,
        "点这里打开公开仓库",
        REPO_URL,
        MARGIN,
        117,
        10.5,
        YELLOW,
    )
    c.setFillColor(TEAL_PALE)
    c.setFont(REGULAR, 8.5)
    c.drawString(MARGIN, 74, "GitHub main 分支是公开最新版来源。")
    c.showPage()


def page_mobile(c, version):
    draw_header(c, "手机 AI", 2, version)
    y = draw_title(
        c,
        "最推荐给普通用户",
        "手机：下载一个文件就能用",
        "适用于豆包、千问，以及其他支持上传文件的 AI 对话。",
    )

    c.setFillColor(TEAL_PALE)
    c.roundRect(MARGIN, y - 46, PAGE_W - MARGIN * 2, 46, 7, fill=1, stroke=0)
    c.setFillColor(TEAL_DARK)
    c.setFont(BOLD, 11.5)
    c.drawString(MARGIN + 18, y - 18, "这里不需要“安装智能体”")
    c.setFont(REGULAR, 10.5)
    c.drawString(MARGIN + 18, y - 35, "只要让当前对话读取 Lite 文件，然后直接问问题。")

    draw_step(
        c,
        1,
        "下载 Lite 中文单文件",
        "点击本页底部链接。文件名是 shawn-nursing-pathway-lite.md。",
        575,
        TEAL,
    )
    draw_step(
        c,
        2,
        "新建对话并上传文件",
        "找到“附件、文件、加号”入口。按钮名称以你手机当前版本为准。",
        500,
        CORAL,
    )
    draw_step(
        c,
        3,
        "发送这一句话",
        "上传成功后，把下面这句话发给 AI。",
        425,
        YELLOW,
    )

    prompt_y = 355
    prompt_h = 108
    c.setFillColor(INK)
    c.roundRect(MARGIN, prompt_y - prompt_h, PAGE_W - MARGIN * 2, prompt_h, 7, fill=1, stroke=0)
    c.setFillColor(YELLOW)
    c.setFont(BOLD, 10)
    c.drawString(MARGIN + 18, prompt_y - 24, "复制这句话")
    draw_wrapped(
        c,
        "请按我上传的 SNP Skill 文件回答。先告诉我这次最值得解决什么；缺少关键信息时只问最少的问题；涉及学校、政策、岗位或工资时，请核验当前官方来源。",
        MARGIN + 18,
        prompt_y - 50,
        PAGE_W - MARGIN * 2 - 36,
        font_size=11.5,
        leading=18,
        color=WHITE,
    )

    draw_card(
        c,
        MARGIN,
        220,
        PAGE_W - MARGIN * 2,
        65,
        "上传不了 .md 文件？",
        "打开 Lite 文件，复制全部文字，粘贴到一个新对话，再发送你的问题。",
        fill=CORAL_PALE,
        accent=CORAL,
        body_size=10.5,
    )

    c.setFillColor(INK)
    c.setFont(BOLD, 11)
    c.drawString(MARGIN, 133, "成功标志")
    c.setFillColor(GRAY)
    c.setFont(REGULAR, 10.5)
    c.drawString(MARGIN, 113, "AI 会先确认你在哪一步，再给最相关的方向和下一步。")
    draw_link(c, "点击下载 Lite 中文单文件", LITE_URL, MARGIN, 80, 11)
    c.showPage()


def page_codex(c, version):
    draw_header(c, "Codex 完整版", 3, version)
    draw_title(
        c,
        "功能最完整",
        "Codex：安装 1 个主入口 + 7 个模块",
        "适合长期使用、继续学习、查最新资料和准备岗位面试。",
    )

    draw_step(
        c,
        1,
        "下载 Suite ZIP",
        "点本页底部链接，下载 shawn-nursing-pathway-suite.zip。",
        615,
        TEAL,
    )
    draw_step(
        c,
        2,
        "解压并复制 8 个 Skill 文件夹",
        "把 ZIP 里 skills/ 下的文件夹复制到 ~/.codex/skills/。",
        535,
        CORAL,
    )
    draw_step(
        c,
        3,
        "重启 Codex 或新建任务",
        "让 Codex 刷新技能列表。",
        455,
        YELLOW,
    )
    draw_step(
        c,
        4,
        "用主入口提问",
        "普通用户只需要记住 $shawn-nursing-pathway。",
        375,
        TEAL,
    )

    prompt_y = 308
    prompt_h = 94
    c.setFillColor(INK)
    c.roundRect(MARGIN, prompt_y - prompt_h, PAGE_W - MARGIN * 2, prompt_h, 7, fill=1, stroke=0)
    c.setFillColor(YELLOW)
    c.setFont(BOLD, 10)
    c.drawString(MARGIN + 18, prompt_y - 24, "第一次测试，直接复制")
    draw_wrapped(
        c,
        "$shawn-nursing-pathway 我是护理本科大二，英语一般，想看看以后有哪些收入更高的路径，我现在先做什么？",
        MARGIN + 18,
        prompt_y - 50,
        PAGE_W - MARGIN * 2 - 36,
        font_size=11.5,
        leading=18,
        color=WHITE,
    )

    draw_card(
        c,
        MARGIN,
        185,
        PAGE_W - MARGIN * 2,
        62,
        "Mac 找不到隐藏目录？",
        "在 Finder 按 Command + Shift + G，输入 ~/.codex/skills/。",
        fill=BLUE_PALE,
        accent=BLUE,
        body_size=10.5,
    )
    draw_link(c, "点击下载 Codex Suite ZIP", SUITE_URL, MARGIN, 88, 11)
    c.showPage()


def page_workbenches(c, version):
    draw_header(c, "智能体工作台", 4, version)
    draw_title(
        c,
        "不用先搭复杂工作流",
        "WorkBuddy、扣子、Dify 等怎么用",
        "先让工具跑起来，再决定要不要增加知识库和工作流。",
    )

    draw_card(
        c,
        MARGIN,
        645,
        PAGE_W - MARGIN * 2,
        126,
        "WorkBuddy / 腾讯云智能体开发平台",
        "下载 WorkBuddy ZIP → 打开“资源中心 > Skills > 自定义 Skills” → 新建并上传 ZIP → 等待格式校验和安全审核。对外只显示一个 SNP Skill 主入口。",
        fill=TEAL_PALE,
        accent=TEAL,
        title_size=14,
        body_size=10.8,
        body_leading=16,
        url=WORKBUDDY_URL,
    )
    draw_link(c, "下载 WorkBuddy Skill ZIP", WORKBUDDY_URL, MARGIN + 18, 532, 10.5)

    draw_card(
        c,
        MARGIN,
        493,
        PAGE_W - MARGIN * 2,
        158,
        "扣子 / Dify / FastGPT / MaxKB / 百炼",
        "第 1 步：把 Lite 文件放进“系统提示词、角色设定、Instructions 或 Prompt”。第 2 步：把 Full 文件上传到“知识库、Knowledge 或文档”。第 3 步：用一个真实问题测试。第一天不需要配置工作流。",
        fill=CORAL_PALE,
        accent=CORAL,
        title_size=14,
        body_size=10.8,
        body_leading=17,
    )
    draw_link(c, "下载 Lite", LITE_URL, MARGIN + 18, 352, 10.5)
    draw_link(c, "下载 Full", FULL_URL, MARGIN + 102, 352, 10.5)

    draw_card(
        c,
        MARGIN,
        315,
        PAGE_W - MARGIN * 2,
        99,
        "不知道自己的平台属于哪一种？",
        "先只上传 Lite 文件。如果回答能先识别你的阶段、再给路径和下一步，就已经能用；需要更多资料时，再加 Full 知识库文件。",
        fill=YELLOW_PALE,
        accent=YELLOW,
        body_size=10.8,
        body_leading=16,
    )

    c.setFillColor(INK)
    c.setFont(BOLD, 11)
    c.drawString(MARGIN, 185, "两个词的对应关系")
    c.setFillColor(GRAY)
    c.setFont(REGULAR, 10.5)
    c.drawString(MARGIN, 163, "系统提示词 / 角色 / Instructions / Prompt → Lite")
    c.drawString(MARGIN, 143, "知识库 / Knowledge / 文档 → Full")
    c.setFillColor(CORAL)
    c.setFont(BOLD, 10)
    c.drawString(MARGIN, 101, "提示：下载后上传的是版本快照，不会自动跟着 GitHub 更新。")
    c.showPage()


def page_prompts(c, version):
    draw_header(c, "开始提问", 5, version)
    draw_title(
        c,
        "不需要学习提示词",
        "直接复制一个真实问题",
        "越具体越好：说清阶段、目标、语言、预算或岗位即可。",
    )

    cards = [
        (
            "1  高考选护理",
            "孩子高考分数一般，护理值得认真了解吗？先看适配和路径。",
            TEAL_PALE,
            TEAL,
        ),
        (
            "2  在读规划",
            "我是护理本科大二，英语一般。想看收入更高的路径，现在先做什么？",
            CORAL_PALE,
            CORAL,
        ),
        (
            "3  护士转岗",
            "我不想一直做临床。请比较国际医院、护理教育、医疗器械和健康科技。",
            YELLOW_PALE,
            YELLOW,
        ),
        (
            "4  海外注册",
            "我是国内注册护士，想了解澳洲 OBA。第一步需要核实什么？",
            BLUE_PALE,
            BLUE,
        ),
        (
            "5  具体薪资",
            "悉尼私立医院 RN 当前大概什么工资？请标年份、来源和税前口径。",
            TEAL_PALE,
            TEAL,
        ),
        (
            "6  核验说法",
            "有人说这条路径能包就业。请把学校、执照、岗位和签证分别核验。",
            CORAL_PALE,
            CORAL,
        ),
    ]
    card_w = (PAGE_W - MARGIN * 2 - 14) / 2
    card_h = 105
    start_y = 635
    for index, (title, body, fill, accent) in enumerate(cards):
        row = index // 2
        col = index % 2
        x = MARGIN + col * (card_w + 14)
        y = start_y - row * 121
        draw_card(
            c,
            x,
            y,
            card_w,
            card_h,
            title,
            body,
            fill=fill,
            accent=accent,
            title_size=11.5,
            body_size=9.8,
            body_leading=14,
        )

    update_y = 247
    update_h = 105
    c.setFillColor(INK)
    c.roundRect(MARGIN, update_y - update_h, PAGE_W - MARGIN * 2, update_h, 7, fill=1, stroke=0)
    c.setFillColor(YELLOW)
    c.setFont(BOLD, 11)
    c.drawString(MARGIN + 18, update_y - 24, "以后怎样更新？")
    draw_wrapped(
        c,
        "GitHub main 分支是最新版。你下载后上传的是一个版本快照；仓库更新后，重新下载同名文件并替换即可。当前公开版本：" + version,
        MARGIN + 18,
        update_y - 49,
        PAGE_W - MARGIN * 2 - 150,
        font_size=10.5,
        leading=16,
        color=WHITE,
    )
    draw_qr(c, REPO_URL, PAGE_W - MARGIN - 84, update_y - update_h + 11, 78)

    c.setFillColor(INK)
    c.setFont(BOLD, 10.5)
    c.drawString(MARGIN, 116, "问问题时写这些就够：")
    c.setFillColor(GRAY)
    c.setFont(REGULAR, 10)
    c.drawString(MARGIN, 96, "当前阶段、学历、语言、预算、目标国家或岗位。证件和完整截图先打码。")
    draw_link(c, "打开 GitHub 公开仓库", REPO_URL, MARGIN, 68, 10.5)
    c.showPage()


def build_pdf(output):
    metadata = json.loads((ROOT / "release.json").read_text(encoding="utf-8"))
    version = metadata["version"]
    output.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(output), pagesize=A4, pageCompression=1)
    c.setTitle("SNP Skill 1 分钟上手指南")
    c.setAuthor("Shawn说护理")
    c.setSubject("SNP Skill 中文优先低门槛使用说明")
    c.setCreator("SNP Skill PDF Builder")

    page_cover(c, version)
    page_mobile(c, version)
    page_codex(c, version)
    page_workbenches(c, version)
    page_prompts(c, version)
    c.save()
    print(f"Built {output}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    build_pdf(args.output.resolve())


if __name__ == "__main__":
    main()
