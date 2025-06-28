from PIL import Image, ImageDraw, ImageFont

def draw_bracket(tournament):
    rounds = tournament.get_all_rounds()
    width = 300 * len(rounds)
    height = max(400, 100 * (2 ** (len(rounds) - 1)))
    img = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", size=20)
    except:
        font = ImageFont.load_default()

    for r, round_matches in enumerate(rounds):
        x = r * 300 + 50
        match_height = height // len(round_matches)
        for i, match in enumerate(round_matches):
            y = i * match_height + match_height // 4
            if isinstance(match, tuple):
                p1, p2 = match
                draw.text((x, y), f"{p1}", font=font, fill="black")
                draw.text((x, y + 30), f"{p2}", font=font, fill="black")
                draw.line([(x - 10, y + 10), (x - 10, y + 40)], fill="gray", width=2)
                draw.line([(x - 10, y + 25), (x, y + 25)], fill="gray", width=2)
            else:
                draw.text((x, y + 15), f"🏆 {match}", font=font, fill="green")

    img.save("bracket.png")