"""Illustration isométrique du coin sport 2 m (dessinée en SVG, à l'échelle en cm)."""
import math
C, S = math.cos(math.radians(30)), 1.55
OX, OY = 165, 145


def P(x, y, z=0):
    return (OX + (x - y) * C * S, OY + (x + y) * 0.5 * S - z * S)


def poly(pts, fill, extra=""):
    d = " ".join(f"{a:.1f},{b:.1f}" for a, b in pts)
    return f'<polygon points="{d}" fill="{fill}" {extra}/>'


def box(x0, y0, z0, x1, y1, z1, top, left, right, cls=""):
    t = poly([P(x0, y0, z1), P(x1, y0, z1), P(x1, y1, z1), P(x0, y1, z1)], top)
    l = poly([P(x0, y1, z0), P(x1, y1, z0), P(x1, y1, z1), P(x0, y1, z1)], left)
    r = poly([P(x1, y0, z0), P(x1, y1, z0), P(x1, y1, z1), P(x1, y0, z1)], right)
    return f'<g class="{cls}">{l}{r}{t}</g>'


def ring(cx, cy, r, z, stroke, w=5):
    pts = [P(cx + r * math.cos(a / 24 * 2 * math.pi), cy + r * math.sin(a / 24 * 2 * math.pi), z) for a in range(24)]
    return poly(pts, "none", f'stroke="{stroke}" stroke-width="{w}" stroke-linejoin="round"')


def scene():
    o = []
    # sol (dalle)
    o.append(box(0, 0, -6, 200, 100, 0, "var(--iso-floor)", "var(--iso-floor-l)", "var(--iso-floor-r)"))
    for x in range(25, 200, 25):
        a, b = P(x, 0), P(x, 100); o.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="var(--iso-grid)" stroke-width="1"/>')
    for y in (25, 50, 75):
        a, b = P(0, y), P(200, y); o.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="var(--iso-grid)" stroke-width="1"/>')
    # cadre de porte + barre de traction (au fond)
    o.append(box(118, -6, 0, 126, 0, 125, "var(--iso-ink)", "var(--iso-ink)", "var(--iso-ink-r)"))
    o.append(box(186, -6, 0, 194, 0, 125, "var(--iso-ink)", "var(--iso-ink)", "var(--iso-ink-r)"))
    o.append(box(118, -6, 125, 194, 0, 131, "var(--iso-ink)", "var(--iso-ink)", "var(--iso-ink-r)"))
    o.append(box(112, -2, 108, 200, 4, 113, "var(--orange)", "var(--iso-or-l)", "var(--iso-or-r)", "float f1"))
    # tapis
    o.append(box(8, 12, 0, 191, 70, 2, "var(--blue)", "var(--iso-blue-l)", "var(--iso-blue-r)"))
    # élastiques (anneaux à plat)
    o.append(f'<g class="float f3">{ring(150, 86, 10, 1, "var(--green)")}{ring(165, 88, 10, 1, "var(--green)")}</g>')
    # haltères
    for yy in (78, 90):
        o.append(f'<g class="float f2">' + box(20, yy, 0, 28, yy + 8, 9, "var(--orange)", "var(--iso-or-l)", "var(--iso-or-r)")
                 + box(28, yy + 2.5, 3, 52, yy + 5.5, 6, "var(--iso-ink)", "var(--iso-ink)", "var(--iso-ink-r)")
                 + box(52, yy, 0, 60, yy + 8, 9, "var(--orange)", "var(--iso-or-l)", "var(--iso-or-r)") + '</g>')
    # kettlebell
    kx, ky = P(100, 88, 10)
    hx, hy = P(100, 88, 24)
    o.append(f'<g class="float f4"><ellipse cx="{kx:.1f}" cy="{ky + 6:.1f}" rx="17" ry="9" fill="var(--iso-shadow)"/>'
             f'<circle cx="{kx:.1f}" cy="{ky - 4:.1f}" r="15" fill="var(--iso-ink)"/>'
             f'<path d="M{hx - 9:.1f} {hy + 8:.1f} C{hx - 9:.1f} {hy - 8:.1f} {hx + 9:.1f} {hy - 8:.1f} {hx + 9:.1f} {hy + 8:.1f}" fill="none" stroke="var(--iso-ink)" stroke-width="5" stroke-linecap="round"/>'
             f'<circle cx="{kx - 5:.1f}" cy="{ky - 9:.1f}" r="4" fill="#fff" opacity=".25"/></g>')
    # cotes
    a, b = P(0, 100, 0), P(200, 100, 0)
    o.append(f'<g class="dim"><line x1="{a[0] - 8:.1f}" y1="{a[1] + 14:.1f}" x2="{b[0] - 8:.1f}" y2="{b[1] + 14:.1f}"/>'
             f'<text x="{(a[0] + b[0]) / 2 - 22:.1f}" y="{(a[1] + b[1]) / 2 + 36:.1f}">2 m</text></g>')
    c, d = P(200, 0, 0), P(200, 100, 0)
    o.append(f'<g class="dim"><line x1="{c[0] + 10:.1f}" y1="{c[1] + 12:.1f}" x2="{d[0] + 10:.1f}" y2="{d[1] + 12:.1f}"/>'
             f'<text x="{(c[0] + d[0]) / 2 + 22:.1f}" y="{(c[1] + d[1]) / 2 + 30:.1f}">1 m</text></g>')
    return ('<svg class="iso" viewBox="0 0 480 430" role="img" aria-label="Illustration d\'un coin sport de 2 mètres sur 1 mètre : '
            'tapis, haltères, kettlebell, élastiques et barre de traction sur un cadre de porte">' + "".join(o) + "</svg>")


if __name__ == "__main__":
    open("/tmp/iso.html", "w").write('<html><head><link rel="stylesheet" href="/home/claude/2m2/src/style.css"></head><body style="padding:40px">' + scene() + "</body></html>")
