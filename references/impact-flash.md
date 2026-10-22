# 冲击帧手册 · 动漫冲击帧（Anime Impact Frame）

> 用途：用户点名「冲击帧 / 黑白爆闪 / impact flash」时启用的画面状态突变模块。
> 做法源自日本动画（ufotable / MAPPA / Trigger）在命中瞬间的单帧～数帧画面突变，比电影式曝光爆闪更短、更狠、更图形化。
> **与两条铁律的关系必须写进稿子**：与铁律 2（禁慢动作）不冲突——冲击帧是瞬间的，不是减速；与铁律 13（禁漫画效果线）不冲突——冲击帧不是「贴在图上的线」，是整幅画面的状态突变。不写这两句，模型会做成「画面上出现一个爆炸的白光球」（违反铁律 13）或拖成慢动作（违反铁律 2）。


<!-- scope-header -->
> **管辖范围**（本文权威负责什么 · 别处更全的指向）
>
> - **本文负责**：**动漫冲击帧（Anime Impact Frame）**：五种闪（白/黑/反色/单色/线稿）· 组合节奏（1/3/5 帧序列）· 时长表 · 五句必留句 · 防扩散三处声明 · 规则段与镜头内模板 · 音效同步 · 六个坑 · H3 推荐组合 · 校验 9 项。
> - **不在本文找**：电影式曝光爆闪（本节一有对照表，但那是另一件事）· 通用特效（→ `vfx-quality.md`）。
> - **权威定义**：与 `heavy-impact-playbook.md` 三·①「命中单帧静止」的区别：那是画面冻结（内容不变），本文件是画面变成纯色/反色/线稿（内容突变）。与 `elemental-barrage.md`「整屏吞没 3 帧」的区别：那是被元素实体填满，本文件是画面变纯色状态。三者写法相近、机制相反，见本文件第十四节。

---

## 一、定位：不是电影曝光爆闪

核心机制：命中的那一瞬，画面丢掉所有细节，变成一张高对比的平面图形——纯黑、纯白、反色、或单色——持续 1–3 帧，然后弹回。

| | 电影曝光爆闪 | 动漫冲击帧 |
|---|---|---|
| 本质 | 整幅画面的过曝 / 欠曝 | 整幅画面的状态突变 |
| 顺序 | 黑 → 白 → 回落 | 反色 / 黑 / 白 / 单色 / 线稿，单独或交替 |
| 时长 | 0.25–1.0 秒 | 1–6 帧（0.04–0.25 秒） |
| 音效 | 压成一条平音 | 一声极短的硬音 |
| 质感 | 电影感、胶片 | 图形化、高对比 |
| 用在哪 | 大片命中、全片最高潮 | 连击中的每一下、重击 |

两者可叠加：先闪 2 帧冲击帧（动漫式），再进 1 秒爆闪（电影式）——「啪一下，然后整个世界白掉」。

---

## 二、五种冲击帧

| 型 | 机制 | 用在哪 | H3 句式 |
|---|---|---|---|
| ① 白闪 | 整幅爆成纯白，所有细节烧掉 | 最通用；重击、术式命中 | `the whole image blows out to solid white, every detail burned away` |
| ② 黑闪 | 整幅沉成纯黑 | 内部冲击（内脏受力、骨折、闷棍）——比白闪更「闷」 | `the whole image snaps to solid black, no detail, no colour, no shape` |
| ③ 反色闪 | 画面颜色全部反转，像底片 | 持续性暴力（连环打击、缠斗中一下重击）——比白闪「更脏」 | `the colours of the whole image invert to their negatives for a single frame, every tone flipped, sky black and shadow white` |
| ④ 单色闪 | 整幅变单一颜色 | 给这一击一个「身份」：能力色 / 元素色 | `the whole image drops to a single flat colour — [血红 / 靛蓝 / 橙] — every other tone gone` |
| ⑤ 高反差线稿帧 | 只剩黑白两色线条，丢掉全部渲染 / 材质 / 光照，像一格手绘关键帧 | 最「动漫」的一种；呼吸法、恶魔形态 | `for a single frame the whole image collapses to flat black and white line art, all rendering, material and light gone, only the contour lines remaining` |

---

## 三、组合节奏：连打 2–4 帧

单个冲击帧太薄，动漫通常连打。三种标准序列：

| 序列 | 拍点 | 节奏读法 | 用在哪 |
|---|---|---|---|
| 标准（3 帧） | 正常 → **反色** → **白闪** → 正常 | 命中那一瞬反色（「啪」）→ 第二帧白闪（「炸」）→ 第三帧回来（「看到结果」） | 通用 |
| 重击（5 帧） | 正常 → **黑闪** → **白闪** → **黑闪** → **白闪** → 正常 | 黑白交替 | 全片最大的一击 |
| 极简（1 帧） | 正常 → **白闪** → 正常 | 只闪一帧 | 快速连击中的每一下 |

---

## 四、时长：写时间不写帧数

| 帧数 | 秒数（24fps） | 观感 | 适用 |
|---|---|---|---|
| 1 帧 | 0.042s | 刺一下，说不清发生了什么 | 连击中的每一下 |
| 2 帧 | 0.083s | 清楚的一闪 | 通用 |
| 3 帧 | 0.125s | 能看清「整个画面变白了」 | 重击 |
| 4–6 帧 | 0.167–0.25s | 定格般的爆发 | 大招、全片最高潮 |
| 7 帧以上 | 0.29s+ | 太长，像卡帧 | 不推荐 |

**必须写具体时间，不能写「很短」。用时间不用帧数**——H3 若不按 24fps 渲染，帧数会错；时间不受帧率影响。

---

## 五、五句绝对不能删（缺一句就翻车）

| 句 | 防什么 |
|---|---|
| `exactly [次数] in the whole video` | 防到处乱加闪 |
| `it is a single-frame picture-state change, not an effect` | 定性——是画面状态突变，不是特效 |
| `not an on-screen light source, not a burst of light inside the picture, not an effect line, not a graphic overlay` | 四重否定——防画出发光球 / 光爆 / 效果线 / 图形叠加 |
| `nothing appears in the picture; the picture itself momentarily becomes something else` | 核心机制——一句话锁死 |
| `no other flashes anywhere` | 总闸 |

---

## 六、防扩散：三个位置同时声明

**只写规则段不够**——实测模型会在收刀、起身、结尾处自发加闪。逐镜重申才是有效的。

| 位置 | 写法 |
|---|---|
| 规则段 | `The flash happens at that one moment and nowhere else: no flash appears during [列举全片其他时间段], and no other flashes anywhere.` |
| 后续每镜 | 各写一句 `There is no flash in this shot.` |
| Structure 段 | `No dissolve, fade, cross-fade, wipe, morph or black frames anywhere other than the single flash above.` |

---

## 七、规则段模板（直接复制，填空）

```
Impact frames, exactly [次数] in the whole video, and they are single-frame picture-state changes, not effects. At [命中时间码], on the exact frame the strike lands, the whole image [闪的类型——blows out to solid white / snaps to solid black / inverts to its negative / drops to a single flat colour / collapses to flat black and white line art]. [如果是多帧序列，写明：This holds for [帧数/时长], then the image returns.] Every detail is gone in that frame: no material, no lighting, no depth, only the flat picture state. This is a change of the whole image itself, not an on-screen light source, not a burst of light inside the picture, not an effect line, not a graphic overlay: nothing appears in the picture; the picture itself momentarily becomes something else. The flash happens at that one moment and nowhere else: no flash appears during [列举全片其他时间段], and no other flashes anywhere.
```

---

## 八、镜头内写法模板（直接复制，填空）

```
单帧白闪：
At [命中时间码] the whole image blows out to solid white for a single frame — every detail, every material and every light gone — and is back to normal on the next frame.

反色 + 白闪序列：
At [命中时间码] the whole image inverts to its negative for one frame — every tone flipped, sky black and shadow white — then blows out to solid white for [帧数] before the colour returns and the world is back.

黑白交替序列：
At [命中时间码] the frame hits black, then white, then black, then white over [帧数] — four flat picture states in a row, no detail in any of them — and on the last frame the world returns in full colour.
```

---

## 九、音效同步：炸一下，不是压平

与电影爆闪相反——电影式是压成一条平音；动漫冲击帧是一声极短的硬音，然后立刻回正常。

```
单帧：The impact frame lands with a single hard sound so short it has no length to it —
      [具体的音，例如 one flat metallic crack / one hard sub-bass hit] — and then the normal
      mix returns on the next frame.

多帧：The impact frames land as [帧数] rapid hits in a row, each one shorter than the last,
      and the mix returns to normal on the final frame.
```

---

## 十、六个坑

| 坑 | 后果 | 防法 |
|---|---|---|
| 不写「整幅画面」 | 模型只闪局部 | `the whole image` 必须写 |
| 不写「丢掉所有细节」 | 闪里还留细节 | `every detail, every material and every light gone` |
| 不写「是画面状态变化不是特效」 | 画出发光球 | 四重否定（第五节第 3 句） |
| 不写「只此一次」 | 到处加闪 | 规则段 + 逐镜重申（第六节） |
| 不写帧数 / 时间 | 闪得太长像卡帧 | 写 `for a single frame` / `for three frames` |
| 忘了写「回落后揭示什么」 | 闪完不知道看什么 | `revealing [具体内容]` |

---

## 十一、H3 推荐组合（实测最稳）

**命中那一帧反色闪（1 帧）→ 白闪（2 帧）→ 第四帧正常画面回来，共 3 帧 = 0.125 秒。**

```
At [时间码] the whole image inverts to its negative for a single frame — every tone flipped, sky black and shadow white — then blows out to solid white for two frames before the colour returns and the world is back.
```

优点：反色帧是「啪」、白闪是「炸」，节奏有层次；总共 0.125 秒够短不拖；两帧白闪给模型留了容错（万一它把反色帧做丢，白闪还在）。

---

## 十二、完整示例（劈雪山 · 单帧白闪）

规则段

```
Impact frame, exactly one in the whole video, and it is a single-frame picture-state change, not an effect. At 00:05.750, on the exact frame the strike lands, the whole image blows out to solid white for three frames, every detail, every material and every light gone — the mountain, the sky, the falling snow and the swordswoman all burned out inside the white. On the fourth frame the world returns in full colour, revealing the red-hot cut line burning across the rock. This is a change of the whole image itself, not an on-screen light source, not a burst of light inside the picture, not an effect line, not a graphic overlay: nothing appears in the picture; the picture itself momentarily becomes something else. The flash happens at that one moment and nowhere else: no flash appears during the draw, during the cut, during the energy's flight before impact, during the sheathing, or at the end of the video, and no other flashes anywhere.
```

镜头内

```
At 00:05.750 the whole image blows out to solid white for three frames — every detail, every material and every light gone — and on the fourth frame the world returns in full colour, revealing the red-hot cut line burning across the rock.
```

收刀镜内逐镜重申：`There is no flash in this shot.`

---

## 十三、校验要点（冲击帧加查，在 21 项之外）

1. 次数：全片冲击帧次数 = 规则段声明的 `exactly [次数]`，逐处对回正文时间码
2. 五句必留句逐句在位（第五节五句，缺一即返工）
3. 三处声明齐全：规则段 + 后续每镜 `There is no flash in this shot.` + Structure 段转场禁令
4. 时长用时间码不用「约」/「很短」；帧数与时间换算自洽（24fps 基准）
5. 定性句在位：`picture-state change, not an effect` + 四重否定 + `nothing appears in the picture`
6. 回落句在位：`revealing [具体内容]`，且揭示内容与本镜动作对得上
7. 与铁律 13 隔离：全稿扫 `radial speed lines` / `speed lines` / `glow orb` 类词 0 命中（冲击帧不是特效，不许写成光球 / 光爆）
8. 与铁律 2 隔离：冲击帧不得写成 `slow / slow-motion / holds for a long beat`
9. 音效层：一声音（或多帧的一串硬音）+ 立刻回正常，不得写成持续低频轰鸣

---

## 十四、与现有规则的关系

- **铁律 2（禁慢动作）**：不冲突。冲击帧是 1–6 帧的瞬间突变，不是减速；稿子里必须显式声明这点，否则模型会把它做成慢放。
- **铁律 13（禁漫画式效果线）**：不冲突。漫画线是「贴在图上的图形」，冲击帧是「整幅画面本身变成另一种状态」——`nothing appears in the picture` 就是这条分界。冲击帧不放开铁律 13，速度线照样 0 命中。
- **`heavy-impact-playbook.md` 三·①「命中单帧静止」**：是另一个工具（画面冻结 = 时间暂停一帧，画面内容不变）；冲击帧是画面内容整体突变成纯色 / 反色 / 线稿。两者可同片并存，也可同一击叠加（先冻结一帧，再进冲击帧序列），但要分别计入各自配额。
- **`vfx-quality.md`**：不冲突。该手册管有魔法设定的特效要高质感；冲击帧根本「不是画面里的东西」（`nothing appears in the picture`），不属特效范畴。
- 与 `elemental-barrage.md`「大面碰撞整屏吞没 3 帧」区分：那是**画面内被元素实体填满**（有材质、有体积）；冲击帧是**画面变成纯色状态**（无材质、无光照、无深度）。写法相近，机制相反。
