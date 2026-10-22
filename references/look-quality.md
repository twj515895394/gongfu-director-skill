# 质感与光影规范（导演定稿口径）

<!-- scope-header -->
> **管辖范围**（本文权威负责什么 · 别处更全的指向）
>
> - **本文负责**：质感与光影：3DCG 取词库（按参考图选支）· 英文默认底块 · 三条红线 · 禁词表 · 入稿适配规则。
> - **不在本文找**：特效质感（→ `vfx-quality.md`）· 水 / 液体材质（→ `water-and-material-quality.md`）。
> - **权威定义**：铁律 14③「质感光影默认块」的**权威定义在这里**；SKILL.md 只做引用。

---

当用户指定质感为 **3DCG / 电影级 CG / 写实渲染** 时，【质感词语】与英文版提示词必须按本文件写。目标：画面读起来像**实拍底板上的东西**，不是游戏过场。文中英文短语可直接复制进提示词。

> 本文件是唯一的质感底块来源。旧底块里的 `next-generation 3D CG`、`Unreal Engine 5 aesthetic`、`subsurface scattering`、`photorealistic CG skin` 已作废（引擎自述 + 皮肤出油元凶），任何稿件不得复活这些词。

## 目录
- 三条命门与五条原则
- 按用途取词库
- 3DCG 的两支词库（A 写实 / B 半写实风格化）
- 三条红线
- 验收判据
- 禁词表（每次生成前必扫）
- 默认英文底块（可直接整块用）
- 入稿时的适配规则（防撞号、防硬套）

## 三条命门

1. 真实的物理（材质 / 重量 / 因果）
2. 真实的介质（空气、体积、雾）
3. 真实的响应（光改变一切，一切也改变光）

## 五条原则（按顺序做）

**原则 1 · 删「引擎自述」**——它是 3D 动漫味的源头。删：`next-generation 3D CG`、`Unreal Engine 5 aesthetic`。换成实拍底板口径：
`photoreal CG rendered to live-action plate standard — real optics, real materials and real dynamics, so every frame reads as a camera recording a real place`
可保留的技术件（描述能力而非风格）：`path-traced global illumination`、`ray-traced reflections`、`volumetric atmosphere`、`PBR materials`、`real fabric and hair simulation`、`ACES colour management`。

**原则 2 · 紧跟反风格化否定**（缺了必跑动漫）：
`no stylistic simplification: no cel-shading, no anime look, no simplified or toy-like geometry, no plastic surfaces, no cartoon squash-and-stretch, no graphic overlays`

**原则 3 · 材料不许死成一个样**（最高频失败点）：
`concrete cracks and spalls` / `steel bends plastically first, then tears` / `glass crazes into a web first, then lets go and falls as sand` / `asphalt shears and folds`。
皮肤近景：`matte dry skin`，光在皮肤上铺开而非热点（`the light spreading across it instead of sitting on it as a hot spot`）；画面里唯一的光泽属于硬表面。皮肤出油元凶，直接删：`subsurface scattering`、`photorealistic CG skin`。

**面部三条补丁**（AI 生脸的高频翻车点，人物镜头必带）：

1. **表情克制**（防面部崩坏）：表情写「收敛」不写「夸张」：`facial expressions stay subtle and contained; even at emotional peaks the face keeps its smooth resting tension, the skin of the cheeks and mouth corners remaining untroubled`。
   - **⚠️ 3DCG 追加（2026-09-28 实测）**：光禁「夸张」不够——**面部发力动词同样会渲出肌肉与纹路**。`pressed down` / `bites down` / `clenched` / `strained` / `tightened` / `grinding` / `forced` / `knitted` / `furrowed` / `trembling` 一律禁用（含否定句）。动作小 ≠ 安全，微发力动作比夸张表情更易漏检。
   - **允许的安全面部动作**：视线方向 · 眨眼 · 瞳孔缩放 · 口型开合度 · 唇的轻微分合 · 呼吸起伏 · 头部角度。
   - **3DCG 情绪四载体**：情绪波动写进 **呼吸 / 肩线 / 重心 / 手的姿态**，脸上不加力。例：`the shoulders settle one notch lower as the breath is let out slowly` 取代 `bites down on the lower lip`。规则全文见 `iron-rules.md` 铁律 14 ①-补。
2. **面部光要软**（防硬阴影）：`the key light wraps softly around the face; facial shadows stay soft and open, never hard-edged`。
3. **皮肤哑光到底**（防油光）：`the skin stays matte with a dry, powder-fine finish; any sheen in frame belongs to hard surfaces, and the face is never one of them`。

**面部约束同样遵守三条红线的第 1 条**（血泪教训）：即使在否定句或 rather than 结构里，也**绝不点名**「咧嘴/大笑/wide grin/皱纹/crease/nasolabial folds」等具象词——模型会拿它当先验执行（写 "rather than a wide grin"，它就给你一个咧嘴大笑）。一律正面句：`a small contained smile` / `the emotion is carried entirely by the eyes` / `her face stays smooth, taut and still`。**面部特写镜头内必须就地重申这句正面约束**，不能只靠全局风格块——镜头内容会稀释全局描述的注意力。

**原则 4 · 空气是介质，不是贴层**：
`dust, ash and steam stay suspended in every shot, light scatters through the volume between camera and subject, distant terrain loses contrast and goes blue`；体积云 `the cloud is volumetric, not a texture`；有风雪雨尘时 `loose particles tear sideways in fast streaks` / `the hair is blown flat sideways and never settles`；静止时降级 `settling when the air is still`。

**原则 5 · 镜头要有光学响应**（纯光效无镜头响应 = 贴图）：
`cinematic lens optics with shallow depth of field`、`natural bokeh`、`subtle lens breathing`、`film-grade highlight rolloff`、`fine film grain`、`low saturation, low contrast, no vignette`。
高能事件的曝光响应链（四条一套，缺一条就假）：点火瞬间收光圈掉几挡 → 最亮处 clip 并 bloom 再回落 → 照亮环境的光维持几帧后快速收回 → `sensor grain responds to the exposure, thickening in the dark and thinning in the bright`。热扰动只能局部（`never a full-frame watery warp`）。

## 按用途取词库

**渲染基底**：`photoreal CG rendered to live-action plate standard` · `volumetric light transport` · `physically based materials` · `fine grain`
**调色/分级**：`low saturation, low contrast, no vignette` · `contrast is structural, not lifted` · `the whole image sits deep in the low end, several stops under a normal exposure, shadows held open but never lifted`
**质量总纲（可当全稿法条）**：`Every object in frame has real mass and a real cause behind its motion.`
**破坏物理（逐条正面句）**：载荷先转移（supports buckle first）→ 破坏沿裂缝传播成前沿（a travelling front，不同时爆开）→ 碎块守恒质量（大块慢起加速、大块停成自然安息角；小块被空气阻力减速、被抛得最远）→ 冲量级联（a hit drives the layer below sideways）→ 落点响应（a ring of dust and a spray cone at the impact point, with a ground shock running out）。
**碎屑三档**：大块（慢、自转、碰撞变向）/ 中块（翻滚快、拖细屑）/ 细尘（读作发光体积雾而非颗粒）——**没有两层同样锐度**。
**特效八正面件**：粒子本身是光源（写清照亮了什么）· 体积雾烟有厚度能藏人 · GI 反弹照亮暗部 · 材质真实反射 · 火焰是流体（有冲击波与碎裂细节）· 魔法具象实体（爪/嘴/身体部位）· 元素有身份色 · 特效与环境交互（被挡/反弹/蔓延）。
**水/液体**：半透明靠厚度读（`the thicker the water the deeper its colour and the less light comes through`），内部分三层（表面浪脊白沫 / 中层气泡帘卷入环境物 / 深层内流更快）；水花、波浪、折射三项必须可数出现。
**纯阴天**：`one continuous overcast ceiling, closed from edge to edge, no readable shape, no variation in tone, no sun anywhere` + `it is the only large bright area in the shot and even it sits low in the exposure` + `flat shadowless grey, nothing outdoors throws a hard shadow`。
**音效质感**：分层（次声轰鸣→材料断裂尖啸→玻璃高频雨→灰落细响），落地给胸腔级冲击；真空环境换载体不换音量（一切经平台传导）；声场随空间换房间（街谷硬反射 / 裂谷长尾混响 / 开阔地几乎无反射）。

## 3DCG 的两支词库（按参考图选支，选定走全稿，不混用）

**A 支 · 写实 CG**（参考图是写实比例人类 / 实拍感场景）→ 用下方「默认英文底块」全文，实拍底板口径。

**B 支 · 半写实风格化 CG**（参考图是动漫脸 / 兽耳 / 风格化比例；用户说「最终幻想那种 CG」也走这支）：

- 总纲：`a high-end big-budget 3D CG video game cutscene — every frame is a meticulously rendered CGI image, never a photograph, never footage, in any light`（写实派负面清单里的 `video-game look / glossy CG render / 3D cartoon / anime shading` 反向印证：`video game cutscene` 和 `CGI` 是拽向游戏 CG 的最强正向锚，明写）
- **暗场 CG 保持条**（夜戏 / 暗场景必写）：`the CG look holds unchanged in any lighting — low light stays clean and noise-free, the faces stay smooth sculpted CG, never photographic`。CG 锚在亮场最容易成立，一暗下来「低光 + 低饱和」就落进模型的真人夜景先验——暗处禁噪点禁颗粒（颗粒 = 摄影），CG 身份必须在暗场显式续命。实测见案例 15。
- **本体定位（B 支最关键的一句）**：`the characters of <Picture N> are interpreted as high-end 3D CG character models — clean digital sculpts with anime-influenced facial proportions and idealized stylized geometry`。形容词（porcelain、stylized）压不住真人化，必须把角色定位成「3D 模型」本体；`anime-influenced facial proportions` 是日厂比例锚——缺它 `3D CG character model` 的先验偏欧美写实游戏脸。参考图是 2D 设定图时禁写 `matching the rendering style of the pictures`（渲染风格匹配 2D 图 = 混合信号，模型折中成 cosplay 照片）——改成「设计照图、渲染是 CG」。实测见案例 11、16。
- 角色：`faces are smooth sculpted CG meshes; the skin is smooth waxy CG skin — an even idealized base tone, no pores, no peach fuzz, no color mottling, a subtle warm translucency glowing through at the cheeks, nose tip and ears, light turning to shadow in one soft warm gradient, micro-texture fine, uniform and low-contrast, specular broad and soft, never a tight glossy hotspot; large crafted CG eyes — a layered iris with radial fibers and color rings, a big crisp specular highlight, a defined waterline; eyebrows as fine painted strands; lips with a soft muted sheen; a small nose, a soft rounded face contour; hair in clean sculpted CG strand clumps with glossy highlights and a clean CG hairline`。**无妆锁必带，且要写正面转移句**：`the faces wear no makeup — the lips keep the same muted matte tone as the rest of the face and the cheeks carry no color of their own, so color on the face comes only from the eyes and hair; facial saturation stays low and facial shading low-contrast`——模型的「美女脸」先验自带浓妆（眼影 / 腮红 / 水光唇），唇同步还会加重唇部妆容；只写 `no makeup` 压不住，必须把唇色/颊色正面转移到「与脸同色、颜色只来自眼和发」。校准要点（FF7RE 截图 + 皮肤渲染文献 + 提示词社区三头印证）：FF 皮肤**不是零纹理零血色**——是均匀底色 + 分区暖透（颊 / 鼻尖 / 耳垂）、明暗交界一条软暖渐变（红光散射最远的物理，禁写 `subsurface scattering` 这个引擎词，写现象）、细而均匀的低对比微纹理、宽软高光（紧高光点 = 油光 = 真人）。比例特征（大眼 / 小鼻 / 圆润轮廓）正面写进词库。反向印证：写实派提示词社区的负面清单（doll-like / wax texture / smooth skin / cgi / 3d render）恰好是拽向 CG 的正向词——`waxy` 放心用。实测见案例 12、13。
- 表情（一做表情最露真人相，必须给 CG 语义）：`facial animation deforms like a stylized CG character rig — restrained and small in amplitude, only a few smooth muscle groups moving, the sculpted features barely shifting from their rest positions even at emotional peaks`。FF 感的关键是**表情幅度小、变形克制**——像高端 CG 面部 rig 的有限 blendshape，不是真人满脸肌肉联动；但禁写 `low-poly` / `low polygon`（会把整体画质拽低），克制感用「restrained / small amplitude / few muscle groups」表达。
- **对话镜表情锁**（法令纹 / 夸张表情的真凶是台词）：含台词（`<d>`）的镜头视同特写镜，必须**镜内就地重申**：`while speaking, the mouth opens just enough to shape the words, only the lips and jaw move, and the rest of the face stays perfectly still and smooth`——唇同步是全脸肌肉联动的最强触发器，只靠全局幅度锁会在台词时刻崩。实测见案例 16。
- 管线词（写实管线只管材质与光，不管脸）：`global illumination` · `ray-traced reflections on hard surfaces` · `PBR materials` · `ambient occlusion` · `soft key light with a gentle rim light` · `shallow depth of field` · `cinematic color grade`
- B 支禁用摄影触发词（会把画面拽向真人实拍）：`path-traced` · `live-action plate standard` · `cinematic lens optics` · `film grain` · `real optics` · `no anime look`
- B 支类别否定清单（必写全；类别级否定合法，不受红线 1 限制）：`no live-action, no real humans, no cosplay, no photographic portrait, no photographic skin texture, no skin pores, no film grain`
- 皮肤不写哑光粉感，写 `uniform porcelain skin shading`（半写实 CG 皮肤带细腻光泽，哑光粉感是 A 支口径）
- 红线 2 不变：作品名（最终幻想等）一个字不进稿，FF 感内化成上述物理描述。
- 参考图里的动漫元素（兽耳 / 尾巴 / 角等）在 B 支下原样保留，只写 `the fox ears and tail exactly as shown in <Picture N>`，不加任何质感形容。

**B 支默认英文底块**（站台争执 v6 实跑验收 + v7 极端版调研加固，可直接整块用，场景句按当轮改写）：

```
Style: a high-end big-budget 3D CG video game cutscene — every frame is a meticulously rendered CGI image, never a photograph, never footage, in any light. The characters are interpreted as high-end 3D CG character models — clean digital sculpts with anime-influenced facial proportions and idealized geometry: faces are smooth sculpted CG meshes; the skin is smooth waxy CG skin with an even idealized base tone — no pores, no peach fuzz, no color mottling — a subtle warm translucency at the cheeks, nose tip and ears, light turning to shadow in one soft warm gradient, micro-texture fine, uniform and low-contrast, specular broad and soft, never a tight glossy hotspot; large crafted CG eyes — a layered iris with radial fibers and color rings, a big crisp specular highlight and a waterline; eyebrows as fine painted strands; the faces wear no makeup — the lips keep the same muted matte tone as the rest of the face and the cheeks carry no color of their own, so color on the face comes only from the eyes and hair; facial saturation stays low and facial shading low-contrast; a small nose, a soft rounded face contour; hair in clean sculpted CG strand clumps with glossy highlights; faces, features and proportions stay exactly as the reference pictures in every frame. Facial animation deforms like a stylized CG character rig — small in amplitude, features barely leaving their sculpted rest positions even at emotional peaks; while speaking, the mouth opens just enough to shape the words, only the lips and jaw move, and the rest of the face stays perfectly still and smooth; emotion reads through the eyes and breath. Lighting and environment follow the scene reference picture exactly — layout, materials, brightness and color temperature — rendered in the same CG film look; the scene brightness is stated explicitly (bright / night) and held in every shot; the CG look holds unchanged in any lighting — low light stays clean and noise-free, the faces stay smooth sculpted CG, never photographic. Shallow depth of field, cinematic color grade, low saturation, low contrast, no vignette. Prohibitions: no live-action, no real humans, no cosplay, no photographic portrait, no photographic skin texture, no film grain, no cel-shading, no plastic surfaces.
```

## 三条红线（比词更重要）

0. **质感承诺是硬线**：用户说 3DCG = 全片必须是 CG 角色、CG 渲染，任何镜头都不许滑向真人实拍；用户没点名「真人」就永远不许出现真人。真实的是管线（材质 / 光 / 物理），不是脸——参考图是风格化角色，角色就保持风格化 CG。校验：`live-action / real place / photoreal` 类词命中时必须确认它修饰的是材质与光、不是角色风格。

1. **否定句不许带动作动词或具象形体名**（模型会把那个词当先验执行：写 no cumulus 它给你积云）。只否性质/颜色：✔ `no readable shape, no defined edges, no variation in tone` ✘ `no cumulus`。把「不许」改写成「必须」：✘ nothing comes to rest → ✔ `the shot is in motion in every single frame`。
2. **作品名一个字不许进稿**（动漫/电影/游戏名都不行，模型会整体复刻那部片）。写具体物理描述，不写「最终幻想那种质感」。
3. **好莱坞的「真」不是更多细节，是更多因果响应**：光有来处、有去处、有东西被它改变。缺响应链，细节堆再多还是 CG 味。

## 验收判据

单帧拎出来问：「它会不会照亮旁边的墙？会不会把地上的水映亮？会不会在玻璃上有倒影？」会 = 高质感；不会 = 贴图。
劣质七病灶（逐条反着查）：塑料感 / PS 渐变火焰 / 过曝光柱 / 满屏马赛克色块 / 预设粒子库 / 省略起势与收势 / 慢镜头注水。

## 禁词表（每次生成前必扫；否定句里命中放行——面部具象词除外，见原则 3 面部补丁）

- 风格类：塑料感/塑料贴片、渐变火焰/廉价渐变、过曝光柱/冲天光柱/金光柱、马赛克/满屏色块、预设粒子库/五毛特效、过曝/光污染
- 引擎自述类（任何语境都禁）：`next-generation 3D CG` · `Unreal Engine 5` · `subsurface scattering` · `photorealistic CG skin`
- 水/液体类：clear · clean · smooth · glass · liquid glass · crystal · glossy · transparent shell · mercury-like · mirror-finish；中文侧：透明壳/玻璃感/液体玻璃/水晶/水银/镜面反光（例外：`ray-traced reflections` 放行，它管引擎能力不管水的读法）
- 自发光类（必须全在否定句里）：辉光/glow · 光环/halo · 能量场/energy field · 魔法阵/magic circle · 符文/runes · 光柱/light beam · 变色/colour change
- 误报提醒：「塑料」只在否定语境放行；合法光束（阳光斜照、低角度掠光）不算冲天光柱。

## 默认英文底块（可直接整块作为 3DCG 质感总纲）

```
Style: photoreal CG rendered to live-action plate standard — a 3D render with real optics, real materials and real dynamics, so every frame reads as a camera recording a real place. Path-traced global illumination, ray-traced reflections, volumetric light transport, physically based materials, real fabric and hair simulation, cinematic lens optics with shallow depth of field, natural bokeh, subtle lens breathing, film-grade highlight rolloff, fine film grain, ACES colour management, low saturation, low contrast, no vignette. No stylistic simplification: no cel-shading, no anime look, no simplified or toy-like geometry, no plastic surfaces, no cartoon squash-and-stretch, no graphic overlays. Surfaces are matte, dry and material-specific: concrete cracks and spalls, steel bends plastically before it tears, glass crazes into a web before it lets go, and no two materials fail the same way. The air is a medium, not a layer: dust, ash and steam stay suspended in it, light scatters through the volume between camera and subject, and distant terrain loses contrast and sinks away. Every object in frame has real mass and a real cause behind its motion. Sensor grain responds to the exposure, thickening in the dark and thinning in the bright. Facial expressions stay subtle and contained — even at emotional peaks the face keeps its smooth resting tension, the skin of the cheeks and mouth corners remaining untroubled; the key light wraps softly around the face and facial shadows stay soft and open; the skin stays matte with a dry, powder-fine finish, and any sheen in frame belongs to hard surfaces, never the face. No text, caption, title, watermark or logo in frame.

The subject is defined entirely by <Picture 1>, held to that image's exact proportions and silhouette; the face is taken only from the leftmost facial close-up cell and is never generated from text. The scene is defined entirely by <Picture 2>, held to that image's layout, materials and light. Where any text in this prompt conflicts with either image, the image wins. No gear, no gloves, no added equipment beyond what the images show.

Light: the light comes only from sources already present in the scene as defined by <Picture 2> — nothing is added: no extra lamp, no flare, no lit fixture beyond what that image already shows. One dominant source sits low relative to the subject and to one side, rimming the outline and lighting the loose strands at the edge of the hair from behind while the face stays in soft shade, and light bounces back up off whatever surfaces are below — floor, ground, water, snow, stone, fabric — into every underside, warming or cooling the shadow according to what it bounces off. The rim light runs down the shoulder, arm, cheekbone, collar and any hanging cloth, thickening and vanishing as the subject turns, and sweeping across the body through any fast movement.

Environment: whatever the environment is doing — wind, snow, rain, dust, spray, drifting particles, moving cloud — it drives through the whole video and never lets up: loose particles tear sideways in fast streaks, any long ribbons or straps snap and whip hard, the hair is blown flat sideways and never settles, and the clothing is pressed hard against the body and blown out again with every gust. These movements are driven by the real environment, never by the camera, and they keep running in every shot.
```

字符预算：约 3,000 字符（H3 单文本项上限 7,000）——总纲其余内容（场景锚具体化 / 贯穿元素定档 / 朝向钉死句 / 分段声明）往里塞时把这笔预算算进去。

与 `vfx-quality.md` 的分工：本块管底片质感（没有魔法也成立）；元素对轰 / 魔法召唤的特效质感仍按 `vfx-quality.md` 写到位，两者叠加不互替。底块的「no extra lamp / no flare」与铁律 7「能力不解释、不视觉化」同口径——不合理移动能力照旧一个字不解释；有魔法设定的特效照旧写满。

## 入稿时的适配规则（防撞号、防硬套）

1. 图号是占位，映射以用户当轮表述为准（硬规则 3：图号由他指定）：
   - 用户说了每图代表什么 → 按他说的映射替换块里的 `<Picture N>`，不问。例：他说「图 1 是 A、图 2 是 B、图 3 是 C 场地」→ 把块里两处 `<Picture 2>`（Scene / Light 段）换成 `<Picture 3>`，并在块后补第二人物的 subject definition（`storyboard-structure.md` 三）。
   - 用户没说（如只说「AB 在 C 对打」，没说什么图是 A / B / C）→ 必须问：「A、B、C 各是图几？」——不问不猜，不自己分配图号。
   - 单人 + 场景，且他说了图 1 是人、图 2 是场景 → 本块原样可用，不必多问。
2. Environment 段的前提：它写的是环境确有风 / 雪 / 雨 / 颗粒时的强档承诺。「never settles / never lets up」只在这前提成立时逐字用；环境静止的片，把该段降级为常规写法（`settling when the air is still`），不许给无风场景硬套永不松懈。
3. Light 段的边界：「低位、一侧、轮廓光」是默认布光描述，不是命令——场景图的光源布局若与此不符（正午顶光、正面平光等），以图为准（块内 "the image wins" 兜底），轮廓光句子按图改写，不硬套。
4. 逐镜不重复：本块一次声明进总纲（持续元素段带 release clause，`storyboard-structure.md` 一）；逐镜只写风力档位变化 / 光源状态的当轮差异，与铁律 14 ② 的既有口径一致。
5. **参考图是风格化 CG 角色时（动漫脸 / 兽耳 / 风格化比例）→ 走 B 支**（见「3DCG 的两支词库」）：总纲 / 角色 / 否定句整组替换，不是只换风格锚一句话——A 支的摄影触发词（`path-traced` / `cinematic lens optics` / `film grain` / `real optics` / `live-action plate standard` / `no anime look`）要逐项扫净，残留任何一个都会把角色拽向真人。每个角色的 subject definition 末尾重申 `appears as the stylized CG character shown in the picture — the same stylized CG face, features and proportions in every frame`。实测见 `generation-feedback.md` 案例 9、10。
6. **亮度锚必须显式**：Style / Light 句必须写死场景亮度（亮场：`stays as brightly and evenly lit as <Picture N> in every shot`；夜场同理写 night）——「以图为准」是冲突兜底不是亮度锚，模型对「地铁 / 室内 / 人工灯」有暗调先验，不声明就按先验走（实测见案例 14，五条全黑夜）。稿内 `dark / dim / fluorescent / glow` 等亮度线索词与参考图冲突时一律改写。

## 何时替换整块

- 用户当轮点名别的质感方向（「高饱和」「浓对比」「去掉颗粒」「卡通渲染」等）→ 只改被点名的句子，其余保留；点名「换个质感」而无具体方向时，先问再换。
- 非超能写实的片（如故意做旧、做粗粝）→ 按点名改写，本块是默认不是铁律。
- **真人实拍感**：写实摄影口径直写，不混用 CG 术语，本块不适用。
- **手绘 / 风格化动画**：按用户指定风格直写，可借用反风格化否定的思路防模型滑回 3D 感。
