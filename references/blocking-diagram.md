# 俯视调度图规格（draw_blocking.py）

<!-- scope-header -->
> **管辖范围**（本文权威负责什么 · 别处更全的指向）
>
> - **本文负责**：俯视调度图 JSON 规格 + `scripts/draw_blocking.py` 绘图规则。
> - **不在本文找**：镜头语言与机位选择逻辑（→ `camera-language.md`）。
> - **权威定义**：硬规则 15「出稿前画调度图」的**规则全文在 `delivery-rules.md`**；本文件只给规格。

---

每个场景生成一张俯视调度图：写一份 JSON 规格，运行 `scripts/draw_blocking.py` 产出 PNG。

```bash
python scripts/draw_blocking.py scene-1-spec.json -o scene-1-blocking.png
# spec 参数也可传 '-' 从 stdin 读（适合脚本管道直接喂 JSON）
python scripts/draw_blocking.py - -o scene-1-blocking.png < scene-1-spec.json
```

## JSON 顶层字段

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `title` | 是 | 图题，如「场景一 · 天台（深夜）」 |
| `size` | 否 | 画布尺寸 `[宽, 高]`，默认 `[10, 8]`，对应场景平面比例 |
| `north` | 否 | 是否画指北针，默认 true |
| `elements` | 是 | 元素数组，见下 |

## 元素类型（elements 数组，按数组顺序绘制）

坐标系：原点在左下角，单位随意但全程一致。建议先把场景平面（墙/门窗/家具/栏杆）定下来，再放角色和机位。

| type | 字段 | 说明 |
| --- | --- | --- |
| `rect` | `xy`（左下角）, `w`, `h`, 可选 `label`/`face`/`edge` | 墙、家具、栏杆、门口等 |
| `label` | `pos`, `text`, 可选 `rotation`/`color` | 自由文字标注（如光源方向） |
| `actor` | `name`（单字母/短名）, `pos`, 可选 `label`/`color`/`label_off` | 角色位置圆点；同名角色自动同色 |
| `move` | `from`, `to`, 可选 `name`（沿用该角色颜色）/`label`/`label_off` | 走位虚线箭头 |
| `axis` | `from`, `to`, 可选 `label`（默认「轴线」） | 主轴线，虚线自动延长到画布边缘 |
| `zone` | `points`（多边形顶点数组）, 可选 `label`/`color` | 机位区阴影，所有机位必须落在区内 |
| `camera` | `name`（如「镜头1」或「镜头3/4」）, `pos`, `look`（朝向点）或 `angle`（度） | 摄影机三角，尖端指向 look |

## 绘图规则（分镜导演必须遵守）

标签防重叠：actor / move 的可选 `label_off` 是 `[dx, dy]` 标签偏移（单位同坐标系）——角色点位密集时（如落点、蹲下、等车位挤在一起）必须用 `label_off` 把标签拉开，画完读图自查：任何两个标签相叠就调偏移重画。

1. **每个场景一张图**，文件名 `scene-N-blocking.png`，存当前工作区。
2. 图内**必须包含**：主轴线（axis）、机位区（zone）、全部摄影机位（camera，name 写对应镜头号）、全部角色的起始位置（actor）与走位（move）。
3. **校验**：所有 camera 的 pos 必须落在 zone 内（即轴线同一侧）；不满足就调整 spec 重画，不允许交付机位跨轴的图。
4. 机位数量与分镜表镜头数对应；正反打共用一个机位区内的相邻机位时可合并标注（如「镜头3/4」）。
5. 交付时调度图与分镜表一起给出，图题与分镜表里的「场景N · 轴线声明」一一对应。

### ⚠️ 两个实测踩过的坑（2026-09-28）

**坑 1 · 机位区不能开太大，否则等于没画。** zone 横跨主轴线的图会「看起来通过校验」——机位落在 zone 内却越了轴。**zone 的上（或下）边界必须严格压在轴线的一侧，并留 0.2 左右余量**（余量给贴着轴线拍的机位）。

**坑 2 · 校验要分两问，别只问一句。** 「在 zone 内」和「在轴线同侧」是两件事，都要逐机位查：

```python
# 逐机位两句必查（缺一句就是事故源）
in_zone  = lo <= y <= hi          # ① 在机位区内
same_side = y < axis_y            # ② 在轴线同一侧（取南侧为例）
```

只看 ① 会漏越轴；只看 ② 会漏「区画小了、机位悬在区外」。**两个都过才算合规。**

**坑 3 · zone 的 zorder 必须高于背景 rect。** 脚本里 zone 曾用 `zorder=0`，被站台/地面等背景矩形（zorder=1）完全盖住——图上根本看不见机位区，人读时无法核对。已修为 `zorder=2.5`（背景 1 < zone 2.5 < 轴线 3 < 机位）。**若某版图上找不到蓝色机位区，先查 zorder，不要怀疑 spec。**

**机位区标签别放区中心**——会被角色圆点压住。贴区顶边（`cy = max(y) - 0.35`，`va="top"`）。

## 完整示例

见 `scripts/example_spec.json`（天台双人对话，含栏杆、楼梯口、走位、轴线、机位区与两个机位）。
