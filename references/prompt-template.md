# 提示词模板 · 动作指导式 T2VA/Ref2VA 结构（用户提供）

> 用途：用户提供的提示词模板骨架。法则全部吸收，格式按下列适配规则修正后使用。


<!-- scope-header -->
> **管辖范围**（本文权威负责什么 · 别处更全的指向）
>
> - **本文负责**：用户模板骨架 + 五大法则（T2VA/Ref2VA 结构参照）。
> - **不在本文找**：交付形态（→ `output-format.md`）· 逐镜结构（→ `storyboard-structure.md`）。
> - **权威定义**：本文件是**格式参照**，不是每次必读。

---

## 一、模板原文骨架

```text
subject_definitions:
<Subject 1> is [角色外观、服装、手部特征（bare hands/no gloves）、格斗流派与招式偏好].
<Subject 2> is [同上].

summary:
[Text-to-Video generation] A [时长] continuous, [风格/氛围] action sequence inside
[场景/空间]. <Subject 1> and <Subject 2> engage in [核心打斗逻辑], featuring
[重点动作与物理反馈] in fluid 1.0x real-time speed without slow motion.

retention_analysis:
N/A - Pure text-to-video generation.        ← 仅 T2VA 时

detailed_description:
The target video is a single continuous [时长] shot rendered in raw 1.0x real-time
speed with a [相机运动方式], high shutter-speed clarity, realistic physical impacts,
and zero slow-motion.
[Shot 1] [总体空间与镜头调度说明]
- From 00:00 to 00:03: [起手爆发动作 + 发力路径 + 对方受击反馈]
- From 00:03 to 00:06.5: [动能转换/受击顺势反击 + 空间位移/环境互动]
- From 00:06.5 to 00:10: [贴身压制/收尾打击 + 镜头轨迹最终收束]

overall_soundscape:
[写实的材质打击声、环境破裂声、衣物摩擦声、短促呼吸声]

non_diegetic_music:
N/A
```

## 二、五大法则（全部吸收进本 skill）

1. 时间轴微观拆解：全片按 2–3 秒一段拆出动能传递段落，每段有明确的
   起手爆发 → 受击反馈 → 顺势转换。多镜稿在 `summary` 里点出三段动能段；
   逐镜拍网格照旧（两套粒度并存：段落管动能、拍管密度）。
2. 动能连贯闭环（Zero Idle）：上一个动作的受击反馈（弯腰/撞墙/踉跄）
   必须顺势成为下一个反击或追击的起始动量。= 铁律 1 + 思路 1 的英文表述，措辞可直接复用：
   `the blocked elbow becomes the hinge his counter swings from`。
3. 生物力学具象动词：禁用 boxing / fight / kungfu 等抽象词。
   词表：`forearm check · elbow strike · low calf kick · palm strike · wrist-trap ·
   shoulder ram · hip toss · shin block · collar tie`。咏春稿配合桥手词
   （tan/bong/gang/fuk sau）混用，一镜至少一个解剖学具体部位词。
4. 防误判硬约束（高价值，必写）：三件套见 `delivery-rules.md`「防误判硬约束」一节，本文件不重列（防拳套 / 防自作主张慢放 / 防动作糊）。
5. 声效与镜头协同：镜头运动与角色移动动量一致；音效精准匹配打击材质
   （`wet elbow thud` / `wall crack` / `short exhale`）。

## 三、与现有体系的冲突修正（用模板前必读）

| 模板原文 | 修正 | 原因 |
|---|---|---|
| `retention_analysis: N/A (Pure T2VA)` | Ref2VA 时不许 N/A——保留参考图锚定 | 我们默认带图 |
| subject_definitions 写"外观、服装" | 有参考图时零外貌描述（铁律 7）——只写 `bare hands / no gloves`（手部事实防拳套）+ 流派 + 行为规则 | 外貌文字与图竞争，模型听文字 → 衣服变了 |
| `single continuous shot`（单镜头） | 默认保留多镜硬切结构（铁律 9）；用户点名要"一镜到底"时才用单镜头版，此时时间轴 3 段拆解写进同一个 shot | 多镜硬切是本 skill 基线 |
| `From 00:00 to 00:03`（3 段粗拆） | 多镜稿中作为 summary 里的动能段概述，逐镜拍网格（0.125s）照旧 | 两套粒度互补，不互替 |
| `1.0x real-time speed` | 与"动作本身 2 倍速"并存不矛盾：渲染 1.0x（防模型降速）+ 编舞 twice natural fight speed | 一个防慢放、一个提速度感 |

## 四、使用顺序

写稿时：本模板的法则 2/3/4/5 直接进 `detailed_description` 与 `subject_definitions`；
法则 1 的三段动能概述进 `summary`。交付前自查防拳套句、zero slow-motion 句、
动能闭环句三件套是否在位。
