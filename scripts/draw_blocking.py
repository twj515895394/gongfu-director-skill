"""Draw a top-down blocking diagram (俯视调度图) from a JSON spec.

Usage:
    python draw_blocking.py spec.json -o scene-1-blocking.png

Spec format: see references/blocking-diagram.md in this skill.
"""
import argparse
import json
import math
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle

ACTOR_COLORS = ["#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6", "#1abc9c"]
CAM_COLOR = "#2c3e50"
AXIS_COLOR = "#e67e22"


def setup_cjk_font():
    candidates = ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC",
                  "PingFang SC", "Source Han Sans SC", "WenQuanYi Zen Hei"]
    installed = {f.name for f in font_manager.fontManager.ttflist}
    for name in candidates:
        if name in installed:
            plt.rcParams["font.family"] = name
            break
    plt.rcParams["axes.unicode_minus"] = False


def extend_line(p1, p2, pad, xlim, ylim):
    """Extend the segment p1-p2 to roughly fill the canvas."""
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    norm = math.hypot(dx, dy) or 1.0
    ux, uy = dx / norm, dy / norm
    reach = (xlim[1] - xlim[0]) + (ylim[1] - ylim[0]) + pad
    return ((p1[0] - ux * reach, p1[1] - uy * reach),
            (p2[0] + ux * reach, p2[1] + uy * reach))


def draw_actor(ax, el):
    pos, r = el["pos"], el.get("r", 0.35)
    color = el.get("color", ACTOR_COLORS[0])
    ax.add_patch(Circle(pos, r, facecolor=color, edgecolor="white", lw=1.5, zorder=6))
    ax.annotate(el["name"], pos, color="white", weight="bold",
                ha="center", va="center", fontsize=11, zorder=7)
    if el.get("label"):
        ldx, ldy = el.get("label_off", [0, 0])
        ax.annotate(el["label"], (pos[0] + ldx, pos[1] - r - 0.25 + ldy), color=color,
                    ha="center", va="top", fontsize=8, zorder=7)


def draw_move(ax, el, fallback_color):
    color = el.get("color", fallback_color)
    arrow = FancyArrowPatch(el["from"], el["to"], arrowstyle="-|>",
                            mutation_scale=18, lw=2, color=color,
                            linestyle=(0, (4, 3)), zorder=5)
    ax.add_patch(arrow)
    if el.get("label"):
        fx, fy = el["from"]
        tx, ty = el["to"]
        ldx, ldy = el.get("label_off", [0, 0])
        ax.annotate(el["label"], ((fx + tx) / 2 + ldx, (fy + ty) / 2 + ldy), color=color,
                    ha="center", va="bottom", fontsize=8, zorder=7)


def draw_camera(ax, el):
    pos = el["pos"]
    look = el.get("look")
    ang = (math.atan2(look[1] - pos[1], look[0] - pos[0]) if look
           else math.radians(el.get("angle", -90)))
    size = el.get("size", 0.55)
    pts = []
    for da, rr in ((0.0, size * 1.6), (2.5, size), (-2.5, size)):
        pts.append((pos[0] + rr * math.cos(ang + da), pos[1] + rr * math.sin(ang + da)))
    ax.add_patch(Polygon(pts, closed=True, facecolor=CAM_COLOR,
                         edgecolor="white", lw=1.2, zorder=8))
    ax.annotate(el["name"], (pos[0], pos[1] + size + 0.2), color=CAM_COLOR,
                weight="bold", ha="center", va="bottom", fontsize=9, zorder=9)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec", help="JSON spec path, or '-' for stdin")
    ap.add_argument("-o", "--out", default="blocking.png")
    ap.add_argument("--dpi", type=int, default=150)
    args = ap.parse_args()

    raw = sys.stdin.read() if args.spec == "-" else open(args.spec, encoding="utf-8").read()
    spec = json.loads(raw)
    setup_cjk_font()

    w, h = spec.get("size", [10, 8])
    xlim, ylim = (-0.5, w + 0.5), (-0.5, h + 0.5)

    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect("equal")
    ax.set_facecolor("#fafafa")
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_color("#cccccc")
    ax.set_title(spec.get("title", ""), fontsize=14, weight="bold", pad=12)

    actor_colors = {}
    for el in spec.get("elements", []):
        t = el["type"]
        if t == "rect":  # wall / furniture / boundary
            xy, rw, rh = el["xy"], el["w"], el["h"]
            ax.add_patch(Rectangle(xy, rw, rh,
                                   facecolor=el.get("face", "#e8e8e8"),
                                   edgecolor=el.get("edge", "#999999"),
                                   hatch=el.get("hatch"), zorder=1))
            if el.get("label"):
                ax.annotate(el["label"], (xy[0] + rw / 2, xy[1] + rh / 2),
                            color="#666666", ha="center", va="center",
                            fontsize=9, zorder=2)
        elif t == "label":
            ax.annotate(el["text"], el["pos"], rotation=el.get("rotation", 0),
                        color=el.get("color", "#888888"), ha="center",
                        va="center", fontsize=9, zorder=2)
        elif t == "actor":
            name = el["name"]
            if name not in actor_colors:
                actor_colors[name] = ACTOR_COLORS[len(actor_colors) % len(ACTOR_COLORS)]
            el.setdefault("color", actor_colors[name])
            draw_actor(ax, el)
        elif t == "move":
            name = el.get("name", "")
            color = el.get("color") or actor_colors.get(name) or \
                ACTOR_COLORS[len(actor_colors) % len(ACTOR_COLORS)]
            draw_move(ax, el, color)
        elif t == "axis":
            p1, p2 = extend_line(tuple(el["from"]), tuple(el["to"]), 0.5, xlim, ylim)
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], "--", color=AXIS_COLOR,
                    lw=1.8, zorder=3)
            label = el.get("label", "轴线")
            mid = ((el["from"][0] + el["to"][0]) / 2, (el["from"][1] + el["to"][1]) / 2)
            ax.annotate(label, mid, color=AXIS_COLOR, weight="bold",
                        ha="center", va="bottom", fontsize=10, zorder=4)
        elif t == "zone":  # camera zone (机位区)
            # zorder=2.5：必须高于背景物（rect=1）与 label（2）、低于轴线（3）与机位
            ax.add_patch(Polygon(el["points"], closed=True,
                                 facecolor=el.get("color", "#ffe9c7"),
                                 edgecolor=AXIS_COLOR, alpha=0.35,
                                 linestyle=":", linewidth=2.0, zorder=2.5))
            if el.get("label"):
                pts = el["points"]
                # 标签贴区顶边，避免被角色点压住
                cx = sum(p[0] for p in pts) / len(pts)
                cy = max(p[1] for p in pts) - 0.35
                ax.annotate(el["label"], (cx, cy), color=AXIS_COLOR,
                            ha="center", va="top", fontsize=9, zorder=2.6)
        elif t == "camera":
            draw_camera(ax, el)
        else:
            raise ValueError(f"unknown element type: {t!r}")

    if spec.get("north", True):
        ax.annotate("N", (xlim[1] - 0.5, ylim[1] - 0.6), ha="center",
                    fontsize=10, weight="bold", color="#999999")
        ax.annotate("", xy=(xlim[1] - 0.5, ylim[1] - 0.8),
                    xytext=(xlim[1] - 0.5, ylim[1] - 1.8),
                    arrowprops=dict(arrowstyle="-|>", color="#999999"))

    fig.tight_layout()
    fig.savefig(args.out, dpi=args.dpi, bbox_inches="tight", facecolor="white")
    print(args.out)


if __name__ == "__main__":
    main()
