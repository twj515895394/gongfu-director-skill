# 实测翻车案例库（生成反馈 → 写法对策）

<!-- scope-header -->
> **管辖范围**（本文权威负责什么 · 别处更全的指向）
>
> - **本文负责**：**实测翻车案例库**：现象 → 根因 → 对策 → 校验词。每条都是真实跑废过的记录。
> - **不在本文找**：规则本体（铁律）。本文件只记录「为什么这条规则存在」。
> - **权威定义**：翻车后**追加于此**。音色性别声明（案例 3）· 分离后悬停方（案例 2）· 锁技接触几何（案例 1)· 起跳翻车（案例 4/5/6）的**案例原文在这里**，各自规则本体在铁律或对应手册。

---

> 来源：真实生成翻车记录，按「现象 → 根因 → 对策 → 校验词」归档。每条都是交付后实测换来的，新案例追加在文末，不许删旧条。

## 案例 1 · 锁技「没夹住」（2026-09-22，瞬身突袭 v3 → v4）

- 现象：写「双腿夹住整条右臂」，生成结果是 A 趴在 B 身上、手臂自由——锁不成形。
- 根因：抽象动词（夹住 / 锁住 / 压制）不给模型可执行的接触点，模型自由发挥。
- 对策：锁技 / 擒拿一律写成接触几何清单——哪条腿压哪侧肩、哪条腿穿哪侧腋、两膝夹哪个部位、手腕固定在谁胸前、胯楔进哪侧肩下。逐项可数，一项都不许省。示例（十字固）：`her right thigh hooking down over <Subject 2>'s right shoulder, her left thigh driving up under <Subject 2>'s right armpit, both knees squeezing <Subject 2>'s upper arm between them` + 地面段 `the arm stretched straight between her thighs, both knees pinched shut, both hands gripping the wrist against her own chest, hips wedged under the shoulder`。
- 校验词：正文出现 `lock / clamp / scissor / pin / armbar` 类词时，必须能逐项指出每个接触部位；指不出来 = 抽象动词回炉。

## 案例 2 · 甩脱后「不动的一方」掉了（2026-09-22，瞬身突袭 v3 → v4）

- 现象：A 被甩出下坠是对的，但 B 也跟着掉下去了——剧本要求 B 悬在 1000 米原位。
- 根因：只写了「动的一方」，没写「不动的一方」；模型默认重力接管画面里所有人。
- 对策：分离 / 甩脱 / 击飞之后留在空中（或原地）的一方，「不动」本身要写成显式动作：`stays exactly where she is at full height, hanging in the air, not falling`。结构段放总闸（`after the release B never drops an inch for the rest of the film`），且逐镜重申——翻转镜 / 甩脱镜 / 坠落镜 / 收尾镜每个分离后的镜头至少一处。
- 校验词：`not dropping / never dropping / not falling / stays exactly / holding her altitude / same altitude`——分离后的每个镜头至少命中一处；某镜 0 命中 = 漏写，该镜必翻车。

## 案例 3 · 男声两轮才杀掉（2026-09-22，瞬身突袭 v4 → v5）

- 现象：只写「两人都是女性 + 无男声」总闸，生成仍是男声发力音；逐人定义音色 + 每声带声源标签后才消除。
- 根因：打斗场景的默认发力音是男声，blanket 声明压不过默认值；铁律 7 的「以图为准」只管画面，管不到音轨——参考图里没有声音信息。
- 对策（五条全做）：
  1. 音效层开头逐人写音色：音区 / 质感 / 发力声形态（如 `a youthful female voice, bright and light in a higher register, her efforts coming out as short crisp exhales`）；
  2. 全片每个发声事件带声源标签 `(S1)` / `(S2)`，不给模型留填空空间；
  3. 开场尽早安排一声该角色的声音（如蓄力镜的吸气），第一时间把声源锚成目标音色；
  4. 禁令三连写全：`no male voice, no deep voice, no growl anywhere`；
  5. 全稿代词与性别一致——脚本扫 `\bhis\b \bhe\b \bhim\b` 应为 0（或仅在否定句）。
- 校验词：`grunt / growl / male` 命中必须全在禁令句；音效层逐个数 `(Sx)` 标签，每个发声事件都有归属。
- 退路：逐人音色仍然压不住 → 删全部人声（零人声 = 零男声），只留环境 / 拳脚 / 布料声，主动告诉用户这是模型偏好问题、不是写法问题。

## 案例 0 · 交付前自查已拦截类（防重复踩坑）

- 装备词误写（`boots` 出现在稿里而图未确认）→ 装备词表脚本扫描是必跑项，命中即改中性词（`feet`）。已在铁律 7 词表，此条只记实测：它真的会漏进来，别跳扫。

## 案例 4 · 过肩摔落地朝向全错（2026-09-28，站台过肩摔 15s 版）

- 现象：B 被过肩摔后 10 条生成视频全部头朝画左，正确物理应头朝画右（惯性前进方向）。
- 根因：镜头描述顺手写了「旋身半周把背贴上 B 的胸前」——B 从身后蒙眼时 A 的背本就贴着 B 的胸，起始体位已成立；多写一个 180° 转身，受力方向整个反转，落点朝向全错。
- 对策：摔投前先写清**起始相对方位**（谁背对谁、谁面朝哪），起始方位直接决定摔投方向；起始体位已成立时**禁止顺手写多余转身**。落地后的头脚朝向必须在俯视调度图上推演一遍，分镜表 / H3 稿 / 调度图三处写死一致（`head pointing frame right, feet pointing frame left`），不许只写「落地」。
- 校验词：`spin / turn / rotate`（写摔投者时）命中必须核对起始方位——起始已背对就不许再转；`lands` 句必须跟头脚朝向（`head pointing frame ...`）。完整五点自查见 `action-physics.md`。

## 案例 5 · 落地瞬间朝向跳变（2026-09-28，站台过肩摔 15s 重跑）

- 现象：摔投滞空段 B 的朝向是一个方向，落地那一帧突然掰成另一个方向，肉眼可见的跳变。
- 根因：提示词写了「双脚甩过头顶」「前翻一圈」（full somersault 语义）+ 只给终点落地姿态。模型对旋转圈数没有概念：按「翻一圈」去转，转到落地前一帧发现与提示词写死的终点朝向不符，就在最后一帧硬掰回来——跳变由此产生。
- 对策：旋转量写死成「绕支点的半周杠杆翻转」（`pivots a half turn over the shoulder like a lever`），滞空中间姿态与落地姿态必须是同一旋转的连续相位（滞空时头已朝向落地方向），同镜内封死加转空间：`one unbroken half-turn from shoulder to ground, no full somersault, no extra spin, no change of facing mid-air`。下一镜开头用状态等式句重申落点朝向（`lies exactly where the throw left her, head toward frame right`）。
- 校验词：`somersault / flip / roll / 前翻 / 后翻 / 翻一圈` 命中时必须能答出「绕哪个支点、转几周、滞空中间姿态的朝向与落地朝向是否同相」；答不出 = 回炉。

## 案例 6 · 落向被指定成反物理（2026-09-28，站台过肩摔 15s 三轮）

- 现象：摔投滞空相位都对，落地那一帧朝向跳变；且摔人者收尾蹲在被摔者脚侧，手腕还扣着——臂长穿帮。
- 根因：落向被写成「前向过肩摔 + 仰面 + 头朝飞行方向」——前向肩摔背落的物理结果只有「头朝摔人者、脚朝飞行方向」（与前滚翻同构）。反物理的终点姿态让模型只能在落地前一帧硬掰，跳变无法靠重跑消除。
- 对策：写摔投前先按「摔法与落向对照」（`action-physics.md` 五点自查末节）定落向；用户指定的落向违反物理时，说明物理结果并给替代摔法/构图，不照写。摔人者收尾位置跟着手腕走——扣着手腕就只能在头侧。
- 校验词：`lands / 落地` 句出现时必答三问：哪种摔法？头朝哪侧（摔人者侧还是飞行方向侧）？摔人者收尾站在哪侧？三答与对照表不一致 = 回炉。

## 案例 7 · 画左/画右凭直觉写，切镜穿帮（2026-09-28，站台争执 v1）

- 现象：镜头3 B 在画右面朝画左，切到镜头4 B 变成面朝画右、A 的肩跑到画右前景——观众读起来像 B 从 A 的左侧瞬移到面前；同稿另有 4 处画面方位写反（建立镜朝向、脚步横移方向、追逐段主导侧、巴掌握势方向）。
- 根因：画面左右是凭直觉写的，没有从俯视调度图逐镜推算；且切镜前后没写状态等式衔接（B 的手还揪在衣领上这件事在镜头4 丢了）。
- 对策：画左/画右一律用公式从调度图推——相机指向目标向量 (dx,dy)，画面右方 = (dy, −dx)；角色朝向向量与之点积，正 = 面朝画右，负 = 面朝画左，逐镜算清再落笔。相邻镜写状态等式衔接（`his hand still gripping her collar exactly as the previous shot left it`）。换机位区时安排骑轴中性镜过渡（主体径直走向/离开镜头深处），避免屏幕方向硬翻。
- 校验词：稿中每个 `frame left / frame right` 命中都必须能答出「这是从调度图哪个机位算出来的」；正反打与追逐段逐镜核对同一角色的画侧是否连续。

## 案例 8 · 耳光拍在头顶上（2026-09-28，站台争执 v1）

- 现象：提示词写「一记正手耳光抽在脸上」，生成的手却抡过头顶、拍在被扇者头顶正中央。
- 根因：只写了挥击轨迹没写死**接触点与打击高度**；轨迹描述里带了上行分量（`sweeps from lower right up toward upper left`），模型把弧线抬过头顶，落点砸在头上。
- 对策：打击动作必写三样——① 接触点：具体部位 + 高度（`the palm lands flush on her left cheek`，脸颊不是头顶）；② 轨迹所在平面：`one level, horizontal forehand arc at cheek height`，弧线与脸齐平，不给上行分量；③ 命中后位移方向与高度锁定：`her head snaps sideways, chin level`——头偏动但下巴保持在同一高度。注意三条红线：否定句里也不许点名「头顶」等具象部位（写了模型就往上打），一律正面句锁定正确落点。
- 校验词：`slap / punch / strike / hit` 句必须同时含接触部位 + 打击高度 + 命中位移方向，缺一样 = 回炉。

## 案例 9 · 3DCG 被拽成真人（2026-09-28，站台争执 v1）

- 现象：参考图是风格化 CG 角色（动漫脸、兽耳），生成的角色却变成真人 / cosplay 照片感——皮肤、五官比例全是真实人类。
- 根因：3DCG 底块里的 `photoreal CG rendered to live-action plate standard` + 反风格化否定里的 `no anime look` 联合作祟——这套组合为写实打斗片调的，遇到风格化 CG 参考图就把角色往真人方向拽，压过了「以图为准」。
- 对策：参考图角色本身是风格化 CG 时，按 `look-quality.md` 入稿适配规则第 5 条**整组走 B 支词库**（总纲 / 角色 / 否定句全换，逐项扫净 A 支摄影触发词）；每个角色的 subject definition 末尾重申 `appears as the stylized CG character shown in the picture — the same stylized CG face, features and proportions in every frame`。材质 / 光 / 物理管线部分不动——要真实的是管线，不是脸。（初版对策只换风格锚一句话，实测压不住，见案例 10。）
- 校验词：`live-action` 命中只能在「风格化 CG 角色」语境之外；参考图是风格化角色时稿内不许出现 `live-action plate standard / no anime look`。

## 案例 10 · 撤了 live-action 仍出真人（2026-09-28，站台争执 v2）

- 现象：按案例 9 换了风格锚、删掉 `live-action plate standard / no anime look` 后重跑，角色仍是真人质感。
- 根因：风格锚换了，但 A 支的摄影触发词残留在稿里（`path-traced / cinematic lens optics / film grain / real optics`）——每个词都在把画面往实拍底板拽，一句话的风格锚顶不住整稿摄影语境；且 skill 此前只有写实 CG 词库，没有「3D CG 动画电影」词库可用。用户点名方向：最终幻想 CG 那种半写实风格化质感。
- 对策：立 B 支词库（`look-quality.md`「3DCG 的两支词库」）——总纲 / 角色 / 管线 / 否定五连**整组替换**，不是只改风格锚一句话；B 支稿逐项扫净摄影触发词。
- 校验词：B 支稿中 `path-traced / live-action / cinematic lens / real optics / photoreal` 应 0 命中，`film grain` 只允许出现在类别否定清单里；类别否定清单必在。

## 案例 11 · B 支仍像 cosplay 照片，一做表情就露真人相（2026-09-28，站台争执 v3）

- 现象：B 支词库整组上稿后重跑，画面仍读作真人 cosplay 照片；角色一做表情，面部肌肉联动完全是真人 rig 的丰富度。
- 根因有二：① 只写了质感形容词（porcelain / stylized），没写**本体定位**——模型把「瓷感皮肤」理解成磨皮真人；且总纲写 `matching the rendering style of the pictures exactly`，参考图是 2D 设定图，渲染风格匹配 2D 图产生混合信号，模型折中成实拍。② 表情只写了「克制」，没写**变形语义**——模型默认按真人面部肌肉系统做表情。
- 对策（三条全做，已并入 `look-quality.md` B 支）：① 本体定位句 `the characters of <Picture N> are interpreted as high-end 3D CG character models — clean digital sculpts with idealized stylized geometry`；参考图是 2D 设定图时禁写「matching the rendering style of the pictures」。② 表情给 CG rig 语义 + 幅度锁：`facial animation deforms like a stylized CG character rig — restrained and small in amplitude, only a few smooth muscle groups moving, the sculpted features barely shifting from their rest positions even at emotional peaks`；禁写 `low-poly`（拽低整体画质）。③ 类别否定清单加 `no cosplay, no photographic portrait`。
- 校验词：`interpreted as ... 3D CG character models / digital sculpt / character rig / small in amplitude` 必在；类别否定清单含 `no cosplay, no photographic portrait`。

## 案例 12 · 建模感有了但皮肤仍像真人（2026-09-28，站台争执 v4）

- 现象：本体定位和 CG rig 表情上稿后，雕塑感出来了，但皮肤仍读作真人——腮红、唇色、肤色斑驳、被光打亮的面部绒毛一应俱全。
- 根因：只锁了「无毛孔 / 无微纹理」的否定，没锁**肤色均匀度**；写实光影管线（GI / 柔和阴影）会自动给皮肤加红晕和色彩变化——均匀白瓷才是参考图那种平面娃娃感的本质。比例特征（大眼 / 小鼻小嘴 / 圆脸廓）也没正面写死，模型默认按写实比例渲染。
- 对策（已并入 `look-quality.md` B 支角色条）：皮肤句升级为「均匀白瓷 albedo + 光只是一道柔和干净的渐变」（`perfectly even pale porcelain albedo ... taking light as one soft clean gradient, facial color staying even and restrained across the whole face`）；比例锁四件正面进稿（`large stylized CG eyes / a small nose and lips / a soft rounded face contour / exactly the reference pictures' proportions`）；发际线加 `a clean CG hairline`；兽耳等动漫元素写显式存在句（`her tall fox ears always stand upright on top of her head`），兼当模型是否认真读图的探针。
- 校验词：`even ... albedo / one soft clean gradient / no peach fuzz / no color mottling`；比例锁四件逐条在稿。（白瓷锁后被案例 13 校准为「蜡质暖透」版，以案例 13 的词为准。）

## 案例 13 · 用 FF7RE 截图做靶标校准皮肤词（2026-09-28，站台争执 v5）

- 现象：案例 12 的「均匀白瓷」上稿后，用户给出 FF7RE 截图作皮肤靶标——白瓷锁过了头：FF 皮肤有分区血色和细均纹理，不是零纹理零血色的平面娃娃。
- 根因：把「去真人感」理解成「去掉一切皮肤信息」。FF7RE 的 CG 感来自四个可控特征：均匀底色 + 分区暖透（颊 / 鼻尖 / 耳垂）、明暗交界一条软暖渐变、细而均匀的低对比微纹理、宽软高光；真人感来自色彩斑驳、紧高光点、绒毛——两组特征不矛盾，锁错一组就翻车。皮肤渲染文献（预积分 / 屏幕空间 SSS 的「润」与「红」）与提示词社区（写实派把 doll-like / wax texture / cgi 当负词）双向印证同一组词。
- 对策：B 支角色条整段换成蜡质暖透版（`look-quality.md` B 支角色条）——`smooth waxy CG skin` + 分区暖透 + 软暖渐变 + 低对比微纹理 + 宽软高光 + 精制 CG 眼（层叠虹膜 / 大高光 / 水线）+ 绘画眉 + 哑光唇。禁写 `subsurface scattering`（引擎词，且是 A 支皮肤出油元凶），只写现象。
- 校验词：`waxy CG skin / warm translucency / one soft warm gradient / low-contrast / broad and soft / layered iris / painted strands / muted sheen` 逐条在稿；`subsurface scattering` 0 命中。

## 案例 14 · 明亮参考图生成全是黑夜（2026-09-28，站台争执 v5 重跑）

- 现象：场景参考图是白天明亮站台，5 条生成全部是黑夜。
- 根因：稿里没有任何显式亮度声明，文本线索却全往暗处指——`fluorescent fixtures`（人工光源 → 模型联想暗室打灯）、`dark track bed`（一个 dark 给全片定暗调）、「地铁站台」先验（地下 = 暗）。「以图为准」是冲突兜底、不是亮度锚——模型先验先走，图拦不住。
- 对策：场景亮度必须**显式声明**并写进 Style/Light 句（`the platform stays as brightly and evenly lit as <Picture 3> in every shot`）+ summary 带亮度词；排查稿内亮度线索词（dark / dim / fluorescent / glow），与参考图亮度冲突的一律改写；亮场场景慎写 rim light 类暗场技法词，要写也必须让位于显式亮度声明。
- 校验词：亮度声明（brightly / daylight / night 其一）必在 Style 或 Light 句和 summary；`dark / dim / fluorescent / glow` 命中必须确认与参考图亮度一致。

## 案例 15 · 一暗就变真人 + 自带浓妆（2026-09-28，站台争执 v6）

- 现象：亮场 CG 感成立后，画面一转暗就完全变真人；且每版人物都被上浓妆——饱和眼影、腮红、水光唇。
- 根因有二：① CG 锚只在亮场成立——低光 + 低饱和低对比恰好落进模型的真人夜景先验，稿里没有「暗场仍是 CG」的声明；② 模型的「美女脸」先验自带妆，稿里从未写 `no makeup`。
- 对策（已并入 `look-quality.md` B 支）：总纲升级为 `a high-end big-budget 3D CG game cinematic ... never a photograph, in any light, in any shot`；布光句加暗场 CG 保持条款（`low light stays clean and noise-free, the faces stay smooth sculpted CG, never photographic`）；角色条加无妆锁（`the faces wear no makeup — lip color muted and natural, cheeks clear and even, the eyes defined by the sculpted lids and lashes alone`）+ 面部低饱和低对比锁（`facial saturation stays low and facial shading low-contrast`）。注意：暗场只是「能保持 CG」，成功率仍是亮场更高——剧情允许就优先亮场。
- 校验词：`in any light / noise-free / never photographic / no makeup / facial saturation stays low` 逐条在稿。
- **验证**：v6 重跑用户验收「质感 OK」（2026-09-28）——B 支词库整组冻结为基准，整块底块见 `look-quality.md`「B 支默认英文底块」。（后续 v7 又按案例 16 加固。）

## 案例 16 · 台词时刻崩：浓妆 + 法令纹 + 滑回真人（2026-09-28，站台争执 v6 复查）

- 现象：v6 静帧质感验收 OK，但说话镜头仍偏真人——口红腮红饱和度高、鼻翼到嘴角挤出夸张法令纹、表情肌肉用力过猛。
- 根因有三：① 法令纹的真凶是**台词**——唇同步是全脸肌肉联动的最强触发器，全局幅度锁在对话镜内被台词稀释（「特写镜内就地重申」原则漏覆盖了对话镜）；② `no makeup` 单词压不过唇同步强化的美妆脸先验，唇部被着重重渲染；③ `3D CG character model` 的模型先验偏**欧美写实游戏脸**（巫师 / 美末路数），缺日厂比例锚，且 `game cinematic` 只写了一次、剂量不够。
- 对策（已并入 `look-quality.md` B 支并更新冻结底块）：① 含台词（`<d>`）的镜头视同特写镜，镜内就地重申 `while speaking, the mouth opens just enough to shape the words, only the lips and jaw move, and the rest of the face stays perfectly still and smooth`；② 妆锁改正面转移句——`the lips keep the same muted matte tone as the rest of the face ... color on the face comes only from the eyes and hair`；③ 总纲升级为 `3D CG video game cutscene` + `CGI`（写实派负面清单词 = CG 正向锚，两头印证），本体定位加 `anime-influenced facial proportions`（日厂比例锚）。
- 校验词：`video game cutscene / CGI / anime-influenced / only the lips and jaw move / muted matte tone` 逐条在稿；每个含 `<d>` 的镜头内必有「只有嘴唇下颌动」重申句。

## 案例 17 · 调度图上的越轴机位：校验只问了一句（2026-09-28，站台质问 v1 用户复查）

- 现象：**用户肉眼在调度图上看出镜头 10 越轴**——它是全片唯一跑到轴线北侧的机位，其余 11 个都在南侧。镜 9→10→11 的左右关系会翻两次，成片必出现「A 回身方向突然反过来」的无台阶越轴。
- 根因有二：① **选位逻辑顺序错了**——先按「这一镜想从哪个角度看」挑机位（A 的右后斜侧），没先筛「必须留在轴线同一侧」；A 站在轴线附近，拍他的右后斜侧就把机位推过轴了。② **机位区开得太大**——zone 横跨了主轴线（y 1.8~7.6，轴线 4.9），机位落在 zone 内，于是「所有 camera 必须落在 zone 内」这句校验**通过了**，越轴没被拦下。
- 第二层坑：**zone 的 zorder=0 被背景盖住**，图上根本看不见机位区——人读时无法核对，用户是靠三角朝向自己看出来的。已修为 zorder=2.5。
- 对策（已并入 `blocking-diagram.md`「两个实测踩过的坑」）：
  1. **zone 边界严格压在轴线一侧 + 留 0.2 余量**，不许横跨轴线。
  2. **校验必须分两问，缺一即事故**：`in_zone = lo <= y <= hi` 且 `same_side = y < axis_y`。
  3. **zorder：背景 rect 1 < zone 2.5 < 轴线 3 < 机位**；图上找不到机位区先查 zorder。
  4. 机位区标签贴区顶边，别放区中心（会被角色圆点压住）。
- 修正动作：镜 10 机位由 A 右后斜侧（北侧越轴）改为 **A 左前斜侧（南侧）**，与镜 9 的追向、镜 11 怒吼朝画右的方向衔接一致。分镜表与 H3 稿同步改写。
- 校验词：交付前逐机位跑两问脚本，输出「违规机位: 无」才算过。

## 案例 18 · 挨打的脸红成一片腮红：否定句点名了「红」（2026-09-28，站台质问 v1 实拍，用户复查）

- 现象：扇耳光后 B 的左脸**整片高饱和粉红色块**，边缘几乎是硬的，像糊了一层腮红妆——不是「被打出来的红」。用户原话：「脸上的红色饱和度太高了，只要很轻微很轻微的就行」。
- 根因（三层，层 1 是真凶）：
  1. **稿里只写了否定句**：`The cheek takes no redness and there is no mark`。**否定句里点名 `redness` = 给模型正向先验**（铁律 7 的死穴），模型把「redness」执行成了整片红。
  2. **没给正面替代描述**：用户说「不留痕」，我只做了「删掉伤」，没给「皮肤保持原样 + 受击血色极轻」的正面句，模型只能在 `redness` 这个唯一线索上自由发挥。
  3. **与常驻底块打架**：B 支有 `cheeks carry no color of their own`，被镜内的 `redness` 直接顶掉——模型选了信号更强的那个。
- 对策（已并入 `iron-rules.md` 铁律 8「脸部受击的红」）：
  1. 正面锚定无变化：`the skin stays the same cool pale tone as the rest of the face`
  2. 红降级成一声呼吸：`no more than the faintest warm flush, low in saturation, fading out before it reaches the jaw, gone within a heartbeat`
  3. **冲击力转交姿态与眼神**：`the face shows the impact entirely through the turn of the head and the set of the eyes, not through colour on the skin`
- 禁令：`flushed / reddened / swollen / bruise / raw` 不许单独成句；不许写大范围渐变（= 腮红）。
- 用户默认口径：**很轻很轻**（要更重他当轮会说）。
- 校验词：镜内搜 `redness / flush / red`，命中必须在 `faintest / barely / low in saturation / fading` 之类降级语境，且同镜必有「同脸同色」正面句 + 「冲击在姿态不在颜色」转移句。

## 案例 19 · 3DCG 表情用力过猛：微小发力动作漏过了自检（2026-09-28，站台质问 v3 实拍，用户复查）

- 现象：B 的近景里 **眉头挤出、牙关咬合外露、下颌绷紧、嘴角牵扯**——是在「演表情」而不是「忍情绪」。用户原话：「**3DCG 人物的表情用力过猛了**」。
- 根因：**不是夸张表情，是微表情里的发力动词**。
  1. 镜 3 写了 `brows pressed down over the eyes`（眉压低）——**主动发力指令**，3DCG 必然渲出皱眉肌与牵扯。
  2. 镜 4 写了 `bites down on the lower lip`（咬住下唇）——**同样是发力动作**，渲成唇部变形 + 下颌肌肉绷起 + 周围纹路。
  3. **铁律 14 原有的自检词表只扫大表情词**（`grinning` / `grimacing` / `wide-eyed` / `nasolabial`），**扫不到 `pressed down` / `bites down` / `strained` 这类小肌肉发力词**——所以自检自己查不出来，这是流程漏洞。
- **关键认知：动作小 ≠ 安全。** 微小发力动作比夸张表情更容易漏检，因为它不触发「夸张」这个关键词。
- 对策（已并入 `iron-rules.md` 铁律 14 ①-补 + `look-quality.md` 面部补丁 1）：
  1. **禁用面部发力动词**：`pressed down` / `bites down` / `clenched` / `strained` / `tightened` / `grinding` / `forced` / `knitted` / `furrowed` / `trembling`（含否定句）。
  2. **允许零肌肉动作**：视线方向 · 眨眼 · 瞳孔缩放 · 口型开合度 · 唇的轻微分合 · 呼吸起伏 · 头部角度。
  3. **3DCG 情绪四载体**：呼吸 / 肩线 / 重心 / 手的姿态。
- 改法对照：`brows pressed down` → `the gaze drops and holds on B's collar, the brow line stays smooth`；`bites down on the lower lip` → `the lips part slightly and close again, the mouth stays soft`；`trembling stops as a swallow is forced down` → `the shoulders settle one notch lower as the breath is let out slowly`。
- 校验词：稿内搜上述 10 个发力词，**0 命中**才算过（含否定句语境）。

## 案例 20 · 同机位同景别切：两条规则同时踩，且规则没进铁律（2026-09-28，站台质问 v3 用户复查）

- 现象：用户截图指出 **镜 3 → 镜 4 几乎是同机位同景别切**——观感像「画面抖了一下又重新对焦」。用户原话：「**这样几乎是同机位同景别切了！这样很违和，你的机位不行！！以后严禁**」。
- 根因（三条）：
  1. **机位夹角过小**：镜 3 过 A 右肩拍 B 正面 · 镜 4 从 B 左前斜侧拍 B —— 两个机位都在 B 的正面环上，夹角目测 <20°（30° 规则要求 ≥30°）。
  2. **景别只跨一档**：镜 3 MCU → 镜 4 CU，只跨一档（规则要求跨两档）。
  3. **根本原因：这条规则只写在 `camera-language.md` 附录 D 的说明句里，没进铁律清单**——编排时没有任何硬卡点拦住它。
- 对策：
  1. **升格为硬规则**，本体写进 `iron-rules.md` 铁律 12「相邻镜硬规则」：相邻同主体镜必须满足「景别跨两档 / 机位夹角 ≥30° / 主体变更」三者之一。
  2. **加进度校验**：第 3 步通用加查第 ⑦ 项逐对核；调度图上量角度，不许目测。
  3. **本片修正**：镜 4 由「B 左前斜侧近景」改为「A 的手腕与 B 的手」**双手大特写**，机位落在 A 正南（夹角 52.9°、景别跨 3 档）——**注意：首轮曾试图改为「B 的眼睛位置拍那双手」，实算夹角只有 6.9°、比原方案更差**，因为手仍在 B 的机位环上。**换机位救不了同主体，必须换主体。** 该镜不出现任何人的脸，顺手卸掉脸的表演压力（与案例 19 联动）。
- 校验词：逐对相邻镜输出「主体是否相同 / 景别跨几档 / 机位夹角」三列，任一不合格即返工。
- 教训：**说明句 ≠ 硬规则。** 只写在参考手册说明里的约束，编排时不会被拦；凡是「以后严禁」级别的，必须进铁律清单 + 校验清单双落位。

## 案例 21 · 动作链断裂：抓衣领的过程被合并镜头并掉了（2026-09-28，站台质问 v4 用户复查）

- 现象：**镜2 还在 B 的靴子急停在 A 脚边，镜3 里 B 的手已经攥住了 A 的衣领**——中间「抬手 → 伸向 → 抓住」整段消失，观众看到手凭空出现在衣领上。用户原话：「**为什么B去伸手抓A衣领的镜头没有了？这个动作都没有了，只有直接已经抓住了，没有之前的动作衔接**」。
- 根因：**v1→v2 做「文戏宁少勿碎」的合并时，把「抓衣领」当成过渡帧并掉了**，只保留结果态。
- **第二层根因：铁律 5 有盲区**——它只管「反应方真不真」，管不到「施动方的动作过程是否被呈现」。所以这个断裂没有被任何规则拦住。
- 对策：
  1. **新增铁律 5-补「动作链完整性」**：凡有交互的动作，施动方必须按「起手 → 接触 → 结果」三段写全。
  2. **警告合并的副作用**：合并只许并「同一动作之内的冗余切点」，**不许并掉整段动作过程**。
  3. 第 3 步加查新增 ⑨ 动作链三段核。
- 修正动作：新增镜3（特写两只手）——`B 扬臂破空、五指张开 → 横向穿过空档 → 五指收拢攥住衣领、立领被攥出褶皱横向带偏`，整只手走完全程；镜数 9→10，15s 重新分配（镜1 让 0.5s、镜2 让 0.3s、台词镜让 0.2s）。
- 校验词：逐个交互动作输出「起手镜号 / 接触镜号 / 结果镜号」三列，任一为空即断链。
- 教训：**「宁少勿碎」的合并有代价。** 合并是切点的优化，不是动作的省略——动作单元是叙事的最小单位，不能当过渡帧删。
