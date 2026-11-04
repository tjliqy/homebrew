# 当前 Git diff 标签核对

基线为 `/data/homebrew` 当前 HEAD，对比工作区。先按同一 JSON 字符串位置比较；标签名称相同则视为保留，即使来源 ID 或别名字段改变。若名称不同，则在同一字符串位置按标签类型和出现顺序配对，记为改名/译名变化；未配对的旧标签才列为删除。英文名按英文源 JSON 中相同字段、同标签类型的出现顺序对齐，无法对齐时用基线名称。

检查 151 个变更 JSON。

## 当前 diff 中未配对的旧 Tag

| 文件 | 类型 | Tag 英文名/基线名称 | 基线中文 Tag | 当前中文 Tag | 次数 |
|---|---|---|---|---|---:|
| `adventure/Kobold Press; 北地萨迦.json` | `book` | Chapter 7: Running a Northlands Campaign | 北地天气 | 无（当前对应位置没有同类型 Tag） | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `condition` | Slowed | 缓慢 | 无（当前对应位置没有同类型 Tag） | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `creature` | Master of Thyles | 提勒斯之主 | 无（当前对应位置没有同类型 Tag） | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `item` | Dagger of Insults | 辱骂匕首 | 无（当前对应位置没有同类型 Tag） | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `item` | Gleipnir | 格莱普尼尔 | 无（当前对应位置没有同类型 Tag） | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `table` | Travel Pace | 旅行步速 | 无（当前对应位置没有同类型 Tag） | 2 |
| `adventure/Kobold Press; 北地萨迦.json` | `table` | Wild Magic Surge | 狂野魔法涌动 | 无（当前对应位置没有同类型 Tag） | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `variantrule` | Ability Score Improvement | 属性值提升 | 无（当前对应位置没有同类型 Tag） | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `variantrule` | Bloodied | 浴血 | 无（当前对应位置没有同类型 Tag） | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `variantrule` | Flyting | 弗律庭 | 无（当前对应位置没有同类型 Tag） | 1 |
| `adventure/The Aciduous Adventurer; 弗里茨·冯·维尔格的奇妙机械宅邸.json` | `table` | Wild Magic Surge | 野魔法涌动 | 无（当前对应位置没有同类型 Tag） | 1 |
| `adventure/Wyatt Trull; 疯法师的地城伴侣书 - 完整版.json` | `race` | Slaad (Green) | 史拉蟾（绿色） | 无（当前对应位置没有同类型 Tag） | 1 |
| `adventure/Wyatt Trull; 疯法师的地城伴侣书 - 完整版.json` | `race` | slaad (green) | 史拉蟾（绿色） | 无（当前对应位置没有同类型 Tag） | 2 |
| `adventure/Wyatt Trull; 疯法师的地城伴侣书 - 完整版.json` | `table` | Shadowfell Despair | 堕影绝望 | 无（当前对应位置没有同类型 Tag） | 3 |
| `book/Bob Starrar; 欢迎来到斯卡西 - 奥术大学.json` | `item` | Griffins - A Field Guide | 狮鹫野外指南 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/Dave Eisinger; 识货商人的价格指南.json` | `item` | Mind Carapace Armor | 心灵外壳护甲 | 无（当前对应位置没有同类型 Tag） | 2 |
| `book/Dungeon Rollers; 先祖武器.json` | `spell` | smite | smite | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/Ghostfire Gaming; 探寻者的扭曲酒馆指南.json` | `condition` | poisoned | 中毒 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/Ghostfire Gaming; 探寻者的扭曲酒馆指南.json` | `condition` | prone | 倒地 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/Ghostfire Gaming; 探寻者的扭曲酒馆指南.json` | `condition` | unconscious | 昏迷 | 无（当前对应位置没有同类型 Tag） | 2 |
| `book/Ghostfire Gaming; 斯蒂布的伙伴圣典.json` | `creature` | Fey Spirit | 妖精灵魄 | 无（当前对应位置没有同类型 Tag） | 4 |
| `book/Ghostfire Gaming; 斯蒂布的伙伴圣典.json` | `creature` | Nobody | 无人 | 无（当前对应位置没有同类型 Tag） | 8 |
| `book/Hipsters & Dragons; 白蝎刺客公会.json` | `monster` | scorpion | 蝎子 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/Jean Lorber; 知识就是力量.json` | `item` | bagpipes | 风笛 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/Jean Lorber; 知识就是力量.json` | `item` | boots | 靴子 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/Jean Lorber; 知识就是力量.json` | `item` | glassblower's tools | 玻璃匠工具 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/Jean Lorber; 知识就是力量.json` | `item` | leatherworking tools | 皮匠工具 | 无（当前对应位置没有同类型 Tag） | 2 |
| `book/MCDM Productions; 阿卡迪亚 第27期.json` | `book` | Beastheart and Monstrous Companions | 怪兽伙伴 | 无（当前对应位置没有同类型 Tag） | 2 |
| `book/MCDM Productions; 阿卡迪亚 第27期.json` | `creature` | Johnny Jones | 约翰尼·琼斯 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/MCDM Productions; 阿卡迪亚 第27期.json` | `item` | rainbow scale boat | 彩虹鳞船 | 无（当前对应位置没有同类型 Tag） | 2 |
| `book/MCDM Productions; 阿卡迪亚 第7期.json` | `book` | The Wild Beyond the Witchlight | 巫光之外的荒野 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/Michael E Shea; 懒惰地下城主的回归.json` | `item` | Stonehewer | 碎岩者 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/Vincent Betternfeld; 符文轮盘赌.json` | `creature` | Devil | 魔鬼 | 无（当前对应位置没有同类型 Tag） | 2 |
| `book/aeyana; 部落之书.json` | `spell` | among others | 等 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/grzart; 神河异界传送指南.json` | `class` | City | 城市 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/grzart; 神河异界传送指南.json` | `class` | warlock | 魔契师 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/grzart; 神河异界传送指南.json` | `class` | wizard | 法师 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/grzart; 神河异界传送指南.json` | `item` | Hacking Tools | 黑客工具 | 无（当前对应位置没有同类型 Tag） | 2 |
| `book/grzart; 神河异界传送指南.json` | `item` | Hacking tools | 黑客工具 | 无（当前对应位置没有同类型 Tag） | 2 |
| `book/grzart; 神河异界传送指南.json` | `item` | hacking tools | 黑客工具 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/grzart; 神河异界传送指南.json` | `spell` | arcane hacking (ua) | 奥术黑客 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/grzart; 神河异界传送指南.json` | `spell` | digital phantom (ua) | 数字幻影 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/grzart; 神河异界传送指南.json` | `spell` | haywire (ua) | 机器失控 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/grzart; 神河异界传送指南.json` | `spell` | infallible relay (ua) | 万无一失中继 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/grzart; 神河异界传送指南.json` | `spell` | invisibility to cameras (ua) | 摄像机隐形 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/grzart; 神河异界传送指南.json` | `spell` | on/off | 开/关 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/grzart; 神河异界传送指南.json` | `spell` | on/off (ua) | 开/关 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/grzart; 神河异界传送指南.json` | `spell` | remote access | 远程访问 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/grzart; 神河异界传送指南.json` | `spell` | remote access (ua) | 远程访问 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/grzart; 神河异界传送指南.json` | `spell` | system backdoor (ua) | 系统后门 | 无（当前对应位置没有同类型 Tag） | 1 |
| `book/grzart; 鞑契异界传送指南.json` | `table` | Random Height and Weight | 随机身高和体重 | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/AgenderArcee; 武艺游侠.json` | `class` | Ranger (Spell-less) | Ranger (Spell-less) | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/AgenderArcee; 武艺游侠.json` | `classFeature` | Call Natural Allies | Call Natural Allies | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/AgenderArcee; 武艺游侠.json` | `table` | Screen; Obscured Areas | Screen; Obscured Areas | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/Benjamin Huffman; 学者Scholar.json` | `spell` | give life | 赐予生命 | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/Benjamin Huffman; 学者Scholar.json` | `spell` | oath-sealing covenant | 誓约封印 | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/Benjamin Huffman; 灵媒Spiritualist.json` | `item` | Spiritualist's pack | Spiritualist's pack | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/Benjamin Huffman; 魔战士Magus.json` | `skill` | Embalmer's tools | Embalmer's tools | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/DanDWiki; 蒙面摔角手.json` | `condition` | 2d10 | 2d10 | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/Dusk Zargoth; 战士重制版.json` | `item` | vehicle | vehicle | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/Dusk Zargoth; 武僧重制版.json` | `optfeature` | Unarmored Movement | 无甲移动 | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/Dusk Zargoth; 野蛮人重制版.json` | `classFeature` | Splash Zone | 泼溅区域 | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/Heavyarms; 铳士.json` | `action` | reaction | reaction | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/Heavyarms; 铳士.json` | `item` | Rounds | 子弹 | 无（当前对应位置没有同类型 Tag） | 6 |
| `class/Heavyarms; 铳士.json` | `item` | Shotshells | 霰弹 | 无（当前对应位置没有同类型 Tag） | 2 |
| `class/Izzy; 化身.json` | `condition` | disease | 疾病 | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/KibblesTasty; 灵能使.json` | `optfeature` | Elemental Discipline | Elemental Discipline | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/KibblesTasty; 灵能使.json` | `optfeature` | Elemental Subclass | Elemental Subclass | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/KibblesTasty; 灵能使.json` | `optfeature` | Shaper Discipline | Shaper Discipline | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/KibblesTasty; 灵能使.json` | `spell` | spatial manipulation | 空间操纵 | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/LaserLlama; 替代法师.json` | `spell` | animate dead (alternate) | 活化死尸（变体） | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/LaserLlama; 替代法师.json` | `spell` | conjure familiar | 咒唤魔宠 | 无（当前对应位置没有同类型 Tag） | 2 |
| `class/LaserLlama; 替代法师.json` | `spell` | polymorph (alternate) | 变形术（变体） | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/LaserLlama; 替代法师.json` | `spell` | shield (alternate) | 护盾术（变体） | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/MCDM Productions; 天赋者与灵能.json` | `condition` | Dash | 疾走 | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/MCDM Productions; 天赋者与灵能.json` | `condition` | Disengage | 撤离 | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/MCDM Productions; 天赋者与灵能.json` | `condition` | Dodge | 回避 | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/MCDM Productions; 邪狱使修订版.json` | `book` | Baleful Interdict | 极恶禁令 | 无（当前对应位置没有同类型 Tag） | 1 |
| `class/MCDM Productions; 邪狱使修订版.json` | `book` | Charm Enemy | 魅惑众敌 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/1985 Games; 胧忆岛：蒿野物语.json` | `item` | 可以护甲 | 可以护甲 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Amellwind; 怪物猎人怪物图鉴.json` | `object` | Dragonator | Dragonator | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Anthony Turco; 柯兰堡文摘：冒险者年鉴.json` | `condition` | lesser restoration | lesser restoration | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `book` | Exploring Eberron | 探索艾伯伦 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `classFeature` | Aura of Courage | 勇气灵光 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `race` | Dwarf (Duergar, Akiak) | Dwarf (Duergar, Akiak) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `spell` | 2d4 | 2d4 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `spell` | astral projection | 星界投射 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `spell` | aura of awe | 敬畏光环 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `spell` | bestial claws | 野兽利爪 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `spell` | blind spot | 盲点 | 无（当前对应位置没有同类型 Tag） | 10 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `spell` | d4 | d4 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `spell` | decelerate | 减速 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `spell` | dream | 梦境术 | 无（当前对应位置没有同类型 Tag） | 5 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `spell` | nomadic gate | 游牧之门 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `spell` | psychometric sense | 感物感知 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `spell` | psychometric touch | 感物之触 | 无（当前对应位置没有同类型 Tag） | 4 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `spell` | psychosomatic feedback | 心身反馈 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `spell` | savage presence | 凶蛮威仪 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `spell` | stomp | 践踏 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `variantrule` | multiclassing | 兼职 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `action` | 协助 | 协助 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `action` | 影响 | 影响 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Avantris; 歪曲之月.json` | `creature` | Dani Jenkin | Dani Jenkin | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | Filthy Jasper | Filthy Jasper | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | Golub Graygullet | Golub Graygullet | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | Stonoga Blackstinger | Stonoga Blackstinger | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 兰德尔·格雷厄姆 | 兰德尔·格雷厄姆 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 凯特格林 | 凯特格林 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 初生吸血鬼 | 初生吸血鬼 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 匪帮队长 | 匪帮队长 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 尸妖 | 尸妖 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 幽魂 | 幽魂 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 木乃伊 | 木乃伊 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 歪曲者 | 歪曲者 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 沃尔特·詹金 | 沃尔特·詹金 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 流浪者 | 流浪者 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 温德尔·索默顿 | 温德尔·索默顿 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 狞笑罪人 | 狞笑罪人 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 玛莎·朗特里 | 玛莎·朗特里 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 维斯拉·棕牙 | 维斯拉·棕牙 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 舒克 | 舒克 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 菲利普·德鲁斯肯瓦尔德 | 菲利普·德鲁斯肯瓦尔德 | 无（当前对应位置没有同类型 Tag） | 4 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 角之王 | 角之王 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 迷途祟魂 | 迷途祟魂 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 邪灵 | 邪灵 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 阿德拉·德鲁斯肯瓦尔德 | 阿德拉·德鲁斯肯瓦尔德 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 鬼火 | 鬼火 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `item` | Calligrapher's Supplies | Calligrapher's Supplies | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `item` | Musical Instrument | Musical Instrument | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `item` | 乐器 | 乐器 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `item` | 书法工具 | 书法工具 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `skill` | Arcana | Arcana | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `skill` | History | History | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Avantris; 歪曲之月.json` | `skill` | Insight | Insight | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `skill` | Investigation | Investigation | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Avantris; 歪曲之月.json` | `skill` | Performance | Performance | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Avantris; 歪曲之月.json` | `skill` | Persuasion | Persuasion | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `skill` | Religion | Religion | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `skill` | 历史 | 历史 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Avantris; 歪曲之月.json` | `skill` | 奥秘 | 奥秘 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `skill` | 威吓 | 威吓 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `skill` | 宗教 | 宗教 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `skill` | 洞悉 | 洞悉 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `skill` | 游说 | 游说 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Avantris; 歪曲之月.json` | `skill` | 表演 | 表演 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Avantris; 歪曲之月.json` | `skill` | 调查 | 调查 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Avantris; 歪曲之月.json` | `variantrule` | Difficult Terrain | 魔法 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `variantrule` | 冷漠【态度】 | 冷漠【态度】 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `variantrule` | 友好【态度】 | 友好【态度】 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Avantris; 歪曲之月.json` | `variantrule` | 敌对【态度】 | 敌对【态度】 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `action` | Disengage | 脱离 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `action` | Dodge | 闪避 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Benevolent Evil; 元素与彼界.json` | `action` | Hide | 隐藏 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `condition` | Acrobatics | Acrobatics | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `creature` | oblex | 蚀心软泥 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Benevolent Evil; 元素与彼界.json` | `creature` | yuan-ti broodguard | 卫雏蛇人 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | Abi-Dalzim's Horrid Wilting | 亚比达奇凋死术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | Primal Savagery | 原初蛮击 | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | Psychic Scream | 心灵尖啸 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | Rizzak's Blazing Lightning | 里扎克的炽焰闪电 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | Toll the Dead | 亡者丧钟 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | acid stream | 酸潮 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | control flames | 控火术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | giant owl | giant owl | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | glacial weapon | 冰川武器 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | killer whale | killer whale | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | mammoth | mammoth | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | ordainment of steel | 钢铁敕令 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | poisoned | poisoned | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | ray of sickness | 疾病射线 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | winter wolf | winter wolf | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `table` | Lingering Injuries | 伤残 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Black Pudding Press; 海马露营者的完全食谱.json` | `spell` | wizard spell list | 法师法术列表 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/DMsGuild; 珊娜萨的其余万事遗失笔记.json` | `condition` | Perception | Perception | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/DMsGuild; 珊娜萨的其余万事遗失笔记.json` | `condition` | regenerate | regenerate | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/DMsGuild; 珊娜萨的其余万事遗失笔记.json` | `creature` | Red-Eye | 红眼 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/DMsGuild; 珊娜萨的其余万事遗失笔记.json` | `creature` | brontosaurus | 雷龙 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/DMsGuild; 珊娜萨的其余万事遗失笔记.json` | `creature` | slaad | 史拉蟾 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/DMsGuild; 珊娜萨的其余万事遗失笔记.json` | `creature` | winged monkey | 飞猴 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/DMsGuild; 珊娜萨的其余万事遗失笔记.json` | `skill` | heal | heal | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/DMsGuild; 珊娜萨的其余万事遗失笔记.json` | `skill` | regenerate | regenerate | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/DMsGuild; 莱瑟曼：无法接近的东方战役指南.json` | `item` | sword | sword | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Darrington Press; 塔尔多雷战役设定集重制版.json` | `item` | shield | 护盾术 | 无（当前对应位置没有同类型 Tag） | 4 |
| `collection/Darrington Press; 塔尔多雷战役设定集重制版.json` | `table` | 分歧的遗迹：进步 | 分歧的遗迹：进步 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Emperror; 恩佩罗的新节奏.json` | `table` | scroll mishaps | 卷轴事故 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `book` | as a reckoning | 作为清算 | 无（当前对应位置没有同类型 Tag） | 9 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `condition` | charmed | 魅惑 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `condition` | exhaustion | 力竭 | 无（当前对应位置没有同类型 Tag） | 4 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `condition` | invisible | 隐形 | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `condition` | poisoned | 中毒 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `condition` | prone | 倒地 | 无（当前对应位置没有同类型 Tag） | 5 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `condition` | restrained | 束缚 | 无（当前对应位置没有同类型 Tag） | 6 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `condition` | unconscious | 昏迷 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `creature` | smoke mephit | 烟魔蝠 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `creature` | steam mephit | 蒸汽魔蝠 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `item` | compass | compass | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `item` | frost brand | 霜铭 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `item` | javelin of lightning | 闪电标枪 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `item` | spear | 矛 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `item` | weapon | weapon | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `spell` | Tenser's floating disk | 谭森浮碟术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `spell` | antimagic field | 反魔法场 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `spell` | cone of cold | 寒冰锥 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `spell` | lesser restoration | 次等复原术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `spell` | see invisibility | 识破隐形 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `table` | Lingering Injuries | 伤患; 伤残 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `table` | lignering injuries | lignering injuries | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `table` | lingering injuries | 伤残 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Genuine Fantasy Press; 被遗忘的秘密合集：觉醒.json` | `condition` | Persuasion | 游说 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆之墟.json` | `item` | amulet | 护身符 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Ghostfire Gaming; 德拉肯海姆之墟.json` | `spell` | shield | 盾牌 | 无（当前对应位置没有同类型 Tag） | 4 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `action` | 反应 | 反应 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `action` | 撤离 | 撤离 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `action` | 研究 | 研究 | 无（当前对应位置没有同类型 Tag） | 38 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `action` | 躲藏 | 躲藏 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `action` | 附赠动作 | 附赠动作 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `action` | 魔法 | 魔法 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `condition` | 冻结 | 冻结 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `condition` | 恐慌 | 恐慌 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `condition` | 污染 | 污染 | 无（当前对应位置没有同类型 Tag） | 19 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `condition` | 虚弱 | 虚弱 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `creature` | 化学家 | 化学家 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `creature` | 巨蘑崽 | 巨蘑崽 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `creature` | 巨鼠怪 | 巨鼠怪 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `creature` | 暗袭鼠怪 | 暗袭鼠怪 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `creature` | 残渣 | 残渣 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `creature` | 炼金鼠士 | 炼金鼠士 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `creature` | 病原师 | 病原师 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `creature` | 老鼠神 | 老鼠神 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `creature` | 邪术巨魔 | 邪术巨魔 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `creature` | 鼠巢守卫 | 鼠巢守卫 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `item` | 修补工具 | 修补工具 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `item` | 工匠工具 | 工匠工具 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `item` | 怪物收获工具（50GP）。 | 怪物收获工具（50GP）。 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `item` | 晶洞 | 晶洞 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `item` | 水晶 | 水晶 | 无（当前对应位置没有同类型 Tag） | 8 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `item` | 炼金工具 | 炼金工具 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `item` | 碎子 | 碎子 | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `item` | 碎片 | 碎片 | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `item` | 维斯特玛王冠 | 维斯特玛王冠 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `item` | 草药工具 | 草药工具 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `item` | 鼓 | 鼓 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | 医药 | 医药 | 无（当前对应位置没有同类型 Tag） | 9 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | 历史 | 历史 | 无（当前对应位置没有同类型 Tag） | 11 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | 奥秘 | 奥秘 | 无（当前对应位置没有同类型 Tag） | 34 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | 宗教 | 宗教 | 无（当前对应位置没有同类型 Tag） | 15 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | 巧手 | 巧手 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | 求生 | 求生 | 无（当前对应位置没有同类型 Tag） | 14 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | 洞悉 | 洞悉 | 无（当前对应位置没有同类型 Tag） | 10 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | 自然 | 自然 | 无（当前对应位置没有同类型 Tag） | 19 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | 调查 | 调查 | 无（当前对应位置没有同类型 Tag） | 11 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | 运动 | 运动 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | 隐匿 | 隐匿 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 任意门 | 任意门 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 传送术 | 传送术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 传送法阵 | 传送法阵 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 侦测思想 | 侦测思想 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 可控突变 | 可控突变 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 定身类人 | 定身类人 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 寻获魔宠 | 寻获魔宠 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 拉瑞心灵联结 | 拉瑞心灵联结 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 探知术 | 探知术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 支配怪物 | 支配怪物 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 污染风暴 | 污染风暴 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 法师护甲 | 法师护甲 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 生物危害 | 生物危害 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 短讯术 | 短讯术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 群体暗示术 | 群体暗示术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 酸雨术 | 酸雨术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 隐形术 | 隐形术 | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 驱逐善恶 | 驱逐善恶 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | 黑暗术 | 黑暗术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `table` | 奥术异常 | 奥术异常 | 无（当前对应位置没有同类型 Tag） | 5 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `variantrule` | Darkness | 黑暗术 | 无（当前对应位置没有同类型 Tag） | 15 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `variantrule` | Immunity | 抗性 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `variantrule` | 优势 | 优势 | 无（当前对应位置没有同类型 Tag） | 42 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `variantrule` | 免疫 | 免疫 | 无（当前对应位置没有同类型 Tag） | 29 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `variantrule` | 劣势 | 劣势 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `variantrule` | 动作 | 动作 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `variantrule` | 反应 | 反应 | 无（当前对应位置没有同类型 Tag） | 5 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `variantrule` | 心灵感应 | 心灵感应 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `variantrule` | 抗性 | 抗性 | 无（当前对应位置没有同类型 Tag） | 19 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `variantrule` | 护甲等级 | 护甲等级 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `variantrule` | 攀爬 | 攀爬 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `variantrule` | 攀爬速度 | 攀爬速度 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `variantrule` | 易伤 | 易伤 | 无（当前对应位置没有同类型 Tag） | 5 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `variantrule` | 生命值 | 生命值 | 无（当前对应位置没有同类型 Tag） | 10 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `variantrule` | 附赠动作 | 附赠动作 | 无（当前对应位置没有同类型 Tag） | 6 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `variantrule` | 附身 | 附身 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Ghostfire Gaming; 鬼魅幽谷 - 玩家指南 - 2024.json` | `action` | 反应 | 反应 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 鬼魅幽谷 - 玩家指南 - 2024.json` | `item` | L | L | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 鬼魅幽谷 - 玩家指南 - 2024.json` | `variantrule` | Proficiency | 黑暗视觉 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Ghostfire Gaming; 鬼魅幽谷 - 玩家指南 - 2024.json` | `variantrule` | 盲视 | 盲视 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Griffin Macaulay; 狮鹫的鞍中珍宝Ⅱ.json` | `item` | Borboss' joyous wand of color | 博博斯的欢乐颜色魔杖 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Griffin Macaulay; 狮鹫的鞍中珍宝Ⅱ.json` | `item` | Nimbus, First Staff of the Thunderbirds | 雨云，雷鸟始杖 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Griffin Macaulay; 狮鹫的鞍中珍宝Ⅱ.json` | `item` | doodle ring | 涂鸦戒指 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Griffin Macaulay; 狮鹫的鞍中珍宝Ⅱ.json` | `item` | dragon turtle barding | 龙龟具装 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Griffin Macaulay; 狮鹫的鞍中珍宝Ⅱ.json` | `item` | spellwoven robes | 织法长袍 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `item` | shield | 护盾术 | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `table` | 附录E: 随机遭遇；沼泽遭遇（1级） | 附录E: 随机遭遇；沼泽遭遇（1级） | 无（当前对应位置没有同类型 Tag） | 4 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `table` | 附录E：随机遭遇；森林遭遇（1-2级） | 附录E：随机遭遇；森林遭遇（1-2级） | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `table` | 附录E：随机遭遇；洞穴遭遇（1级） | 附录E：随机遭遇；洞穴遭遇（1级） | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `table` | 附录E：随机遭遇；焦土林遭遇（等级3） | 附录E：随机遭遇；焦土林遭遇（等级3） | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Hit Point Press; 谦卑林故事集.json` | `item` | shield | 护盾术 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/James Ohlen; 博德之门的英雄们.json` | `creature` | 盗贼 | 盗贼 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Kobold Press; 北地世界书.json` | `condition` | d12 | d12 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Kobold Press; 北地世界书.json` | `creature` | Monster Hunter | 怪物猎人 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Kobold Press; 北地世界书.json` | `creature` | Werekin | 兽化裔 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Kobold Press; 北地世界书.json` | `race` | Ratatosk | 树鼠族 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Kobold Press; 北地世界书.json` | `race` | Ravenfolk | 鸦族 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Kobold Press; 北地世界书.json` | `spell` | Fiery Siege | 烈焰攻城 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Kobold Press; 北地世界书.json` | `spell` | Noble Sacrifice | 高贵牺牲 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Kobold Press; 北地世界书.json` | `spell` | Pawn of the Wyrd | 玄命的棋子 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Kobold Press; 北地世界书.json` | `spell` | Song of the Shield Wall | 盾墙之歌 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Kobold Press; 北地世界书.json` | `spell` | Storm Maiden's Edge | 风暴少女之刃 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Kobold Press; 北地世界书.json` | `spell` | Valhalla's Cohort | 瓦尔哈拉战团 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Kobold Press; 北地世界书.json` | `table` | Travel Pace | 旅行步速 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Kobold Press; 北地世界书.json` | `variantrule` | Opportunity Attack | 借机攻击 | 无（当前对应位置没有同类型 Tag） | 4 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `action` | Dash | 疾走 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `action` | Disengage | 撤离 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `action` | Dodge | 回避 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `action` | Magic | 魔法 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `book` | Tasha's Cauldron of Everything | 塔莎的万事坩埚 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `condition` | blinded | 目盲 | 无（当前对应位置没有同类型 Tag） | 5 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `condition` | charmed | 魅惑 | 无（当前对应位置没有同类型 Tag） | 5 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `condition` | deafened | 耳聋 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `condition` | exhaustion | 力竭 | 无（当前对应位置没有同类型 Tag） | 5 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `condition` | frightened | 恐慌 | 无（当前对应位置没有同类型 Tag） | 4 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `condition` | paralyzed | 麻痹 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `condition` | petrified | 束缚 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `condition` | petrified | 石化 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `condition` | poisoned | 中毒 | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `condition` | prone | 倒地 | 无（当前对应位置没有同类型 Tag） | 10 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `condition` | restrained | 石化 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `condition` | stunned | 震慑 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `condition` | unconscious | 昏迷 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `condition` | 魅惑 | 魅惑 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Bola of Big Game (Rare) | Bola of Big Game (Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Bola of Big Game (Uncommon) | Bola of Big Game (Uncommon) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Celestial Feather (Rare) | Celestial Feather (Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Celestial Feather (Uncommon) | Celestial Feather (Uncommon) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Celestial Feather (Very Rare) | Celestial Feather (Very Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Cloak of Adventuring | Cloak of Adventuring | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Dragon Heart (Legendary) | Dragon Heart (Legendary) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Dragon Heart (Rare) | Dragon Heart (Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Dragon Heart (Very Rare) | Dragon Heart (Very Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Eldritch Whetstone (Legendary) | Eldritch Whetstone (Legendary) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Eldritch Whetstone (Rare) | Eldritch Whetstone (Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Eldritch Whetstone (Uncommon) | Eldritch Whetstone (Uncommon) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Eldritch Whetstone (Very Rare) | Eldritch Whetstone (Very Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Enchanted Garment (Legendary) | Enchanted Garment (Legendary) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Enchanted Garment (Rare) | Enchanted Garment (Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Enchanted Garment (Very Rare) | Enchanted Garment (Very Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Enchanted Inks (Common) | Enchanted Inks (Common) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Enchanted Inks (Legendary) | Enchanted Inks (Legendary) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Enchanted Inks (Rare) | Enchanted Inks (Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Enchanted Inks (Uncommon) | Enchanted Inks (Uncommon) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Enchanted Inks (Very Rare) | Enchanted Inks (Very Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Ensorcelled Blackpowder (Common) | Ensorcelled Blackpowder (Common) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Ensorcelled Blackpowder (Rare) | Ensorcelled Blackpowder (Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Ensorcelled Blackpowder (Uncommon) | Ensorcelled Blackpowder (Uncommon) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Hammer of Thunderbolts | 雷神之锤 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Headband of the Sifu's Favor (Legendary) | Headband of the Sifu's Favor (Legendary) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Headband of the Sifu's Favor (Rare) | Headband of the Sifu's Favor (Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Headband of the Sifu's Favor (Uncommon) | Headband of the Sifu's Favor (Uncommon) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Headband of the Sifu's Favor (Very Rare) | Headband of the Sifu's Favor (Very Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Hood of Hearing | Hood of Hearing | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Loyal Projectile (Common) | Loyal Projectile (Common) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Loyal Projectile (Rare) | Loyal Projectile (Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Loyal Projectile (Uncommon) | Loyal Projectile (Uncommon) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Loyal Projectile (Very Rare) | Loyal Projectile (Very Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Mask of Heroic Cunning | Mask of Heroic Cunning | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Monster and Spawn Reunion (Rare) | Monster and Spawn Reunion (Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Monster and Spawn Reunion (Very Rare) | Monster and Spawn Reunion (Very Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Phoenix Down Feather (Rare) | Phoenix Down Feather (Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Phoenix Down Feather (Uncommon) | Phoenix Down Feather (Uncommon) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Phoenix Down Feather (Very Rare) | Phoenix Down Feather (Very Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Ring of Weaving | Ring of Weaving | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Spiked Collar (Rare) | Spiked Collar (Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Spiked Collar (Uncommon) | Spiked Collar (Uncommon) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Spiked Collar (Very Rare) | Spiked Collar (Very Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Studded Collar (Rare) | Studded Collar (Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Studded Collar (Uncommon) | Studded Collar (Uncommon) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Studded Collar (Very Rare) | Studded Collar (Very Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Tome of Slaying (Legendary) | Tome of Slaying (Legendary) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Tome of Slaying (Rare) | Tome of Slaying (Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Tome of Slaying (Very Rare) | Tome of Slaying (Very Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Weavesaber (Legendary) | Weavesaber (Legendary) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Weavesaber (Rare) | Weavesaber (Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Weavesaber (Uncommon) | Weavesaber (Uncommon) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | Weavesaber (Very Rare) | Weavesaber (Very Rare) | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | armor of blood drinking | armor of blood drinking | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | belt of fire giant strength | 火巨人力量腰带 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | blindfold of seeing | blindfold of seeing | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | boots of trekking | boots of trekking | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | cape of heroic presence | cape of heroic presence | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | cloak of adventuring | cloak of adventuring | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | disguise kit | 易容工具 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | forgery kit | 文书伪造工具 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | gauntlets of ogre power | 食人魔力量护手 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | hammer of thunderbolts | 雷神之锤 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | helm of exsanguination | helm of exsanguination | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | herbalism kit | 草药工具 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | hood of hearing | hood of hearing | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | mask of heroic cunning | mask of heroic cunning | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | muffle of speech | muffle of speech | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | poisoner's kit | 毒药工具 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | ring of weaving | ring of weaving | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | rod of wefting | rod of wefting | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | staff of wandering | staff of wandering | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | suit of heroic prowess | suit of heroic prowess | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | thieves' tools | 盗贼工具 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | wand of warping | wand of warping | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | weapon of bloodletting | weapon of bloodletting | 无（当前对应位置没有同类型 Tag） | 4 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `item` | 放血之盔 | 放血之盔 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `skill` | Arcana | 奥秘 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `skill` | History | 历史 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `skill` | Investigation | 调查 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `skill` | Perception | 察觉 | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `skill` | Performance | 表演 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `skill` | Sleight of Hand | 巧手 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `skill` | Stealth | 隐匿 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `skill` | Survival | 求生 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | Beast bond | 兽之联结 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | Bigby's hand | 毕格比之手 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | Charm person | 魅惑类人 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | Create or destroy water | 造水术/枯水术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | Dissonant whispers | 不谐低语 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | Entangle | 纠缠术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | Goodberry | 神莓术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | Ice knife | 冰刃 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | Otto's irresistible dance | 奥图迷舞 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | Purify food and drink | 净化饮食 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | Thunderwave | 雷鸣波 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | alarm | 警报术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | alter self | 变身术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | animal shapes | 动物形态 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | animate objects | 活化物件 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | arcane lock | 秘法锁 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | augury | 卜筮术 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | aura of life | 生命灵光 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | awaken | 启蒙术 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | bane | 灾祸术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | banishment | 放逐术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | barkskin | 树肤术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | bless | 祝福术 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | blight | 枯萎术 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | blinding smite | 致盲斩 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | blindness/deafness | 目盲术/耳聋术 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | branding smite | 印记斩 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | call lightning | 召雷术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | calm emotions | 安定心神 | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | chaos weapon | chaos weapon | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | charm monster | 魅惑怪物 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | charm person | 魅惑类人 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | chromatic orb | 繁彩球 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | clairvoyance | 鹰眼术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | cloud of daggers | 匕首之云 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | cloudkill | 死云术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | color spray | 七彩喷射 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | commune | 通神术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | compulsion | 强迫术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | cone of cold | 寒冰锥 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | confusion | 困惑术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | conjure animals | 咒唤兽群 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | conjure elemental | 咒唤元素 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | conjure woodland beings | 咒唤林地卫士 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | contagion | 疫病术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | create or destroy water | 造水术/枯水术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | cure wounds | 疗伤术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | darkness | 黑暗术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | daylight | 昼明术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | detect evil and good | 侦测善恶 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | detect magic | 侦测魔法 | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | detect poison and disease | 树肤术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | detect thoughts | 侦测思想 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | disintegrate | 解离术 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | dispel evil and good | 驱逐善恶 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | dispelling smite | dispelling smite | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | dissonant whispers | 不谐低语 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | divine word | 圣言术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | dominate monster | 支配怪物 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | dream of the blue veil | 蓝纱一梦 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | druidcraft | 德鲁伊伎俩 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | dust devil | 龙卷尘暴 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | earthbind | 地缚 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | eldritch blast | 魔能爆 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | elemental weapon | 元素武器 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | enemies abound | 敌群环绕 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | enervation | 汲能术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | enhance ability | 强化属性 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | enlarge/reduce | 变巨/缩小术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | entangle | 侦测毒性和疾病 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | entangle | 纠缠术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | faerie fire | 妖火 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | fear | 恐惧术 | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | find greater familiar | find greater familiar | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | flesh to stone | 石化术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | fly | 飞行术 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | geas | 指使术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | grasping vine | 擒抱藤 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | grease | 油腻术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | guardian of nature | 自然守卫 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | guiding weapon | guiding weapon | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | harm | 重伤术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | heal | 医疗术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | hex | 脆弱诅咒 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | hold monster | 定身怪物 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | hold person | 定身类人 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | holy weapon | 神圣武器 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | hypnotic pattern | 催眠图纹 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | identify | 鉴定术 | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | insect plague | 疫病虫群 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | invisibility | 隐形术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | invisible weapon | invisible weapon | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | lesser restoration | 次等复原术 | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | light | 光亮术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | lightning bolt | 闪电束 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | locate creature | 生物定位术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | locate object | 物件定位术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | maelstrom | 大漩涡 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | mage armor | 法师护甲 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | magic missile | 魔法飞弹 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | magic weapon | 魔化武器 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | mass cure wounds | 群体疗伤术 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | mass healing word | 群体治愈真言 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | mass suggestion | 群体暗示术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | meld into stone | 融身入石 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | message | 传讯术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | nondetection | 回避侦测 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | pass without trace | 纠缠术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | pass without trace | 行动无踪 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | plane shift | 位面转移 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | plant growth | 植物滋长 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | polymorph | 变形术 | 无（当前对应位置没有同类型 Tag） | 8 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | primordial weapon | primordial weapon | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | programmed illusion | 预置幻影 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | protection from evil and good | 防护善恶 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | protection from poison | 防护毒素 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | raise dead | 死者复活 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | reaping smite | reaping smite | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | reincarnate | 转生术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | remove curse | 移除诅咒 | 无（当前对应位置没有同类型 Tag） | 10 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | resurrection | 复生术 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | revivify | 回生术 | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | root snare | root snare | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | scorching ray | 灼热射线 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | scrying | 探知术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | searing smite | 炽焰斩 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | sending | 短讯术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | shatter | 粉碎音波 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | shield of faith | 虔诚护盾 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | shillelagh | 行动无踪 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | silence | 沉默术 | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | skill empowerment | 授予技能 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | sleep | 睡眠术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | sleet storm | 雪雨暴 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | slow | 缓慢术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | spare the dying | 维生术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | speak with dead | 死者交谈 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | speak with plants | 植物交谈 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | spirit guardians | 灵体卫士 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | spiritual weapon | 灵体武器 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | staggering smite | 惊惧斩 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | stinking cloud | 臭云术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | stoneskin | 石肤术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | suggestion | 暗示术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | summon aberration | 异怪召唤术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | summon beast | 野兽召唤术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | summon celestial | 天界召唤术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | summon construct | 构装召唤术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | summon elemental | 元素召唤术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | summon fey | 妖精召唤术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | summon fiend | 邪魔召唤术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | summon shadowspawn | 暗影衍体召唤术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | summon undead | 亡灵召唤术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | sundering smite | 崩解圣斩 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | telekinesis | 心灵遥控 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | teleportation circle | 传送法阵 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | thorn whip | 橡棍术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | thorn whip | 荆棘之鞭 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | thunderclap | 鸣雷破 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | thundering smite | thundering smite | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | transport via plants | 木遁术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | tree stride | 树跃术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | unseen servant | 隐形仆役 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | vampiric touch | 吸血鬼之触 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | vampiric weapon | vampiric weapon | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | vengeful smite | vengeful smite | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | wall of sand | 沙墙术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | wall of stone | 石墙术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | wall of thorns | 棘墙术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | warding bond | 守护之链 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | warding smite | warding smite | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | water breathing | 水下呼吸 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | water walk | 水上行走 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | wish | 祈愿术 | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | wrath of nature | 自然之怒 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | wrathful smite | 激愤斩 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | 荆棘之鞭 | 荆棘之鞭 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `variantrule` | Bright Light | 明亮光照 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `variantrule` | Darkness | 黑暗 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `variantrule` | Dim Light | 微光光照 | 无（当前对应位置没有同类型 Tag） | 4 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `variantrule` | Fly Speed | 飞行速度 | 无（当前对应位置没有同类型 Tag） | 3 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `variantrule` | Long Rest | 长休 | 无（当前对应位置没有同类型 Tag） | 8 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `variantrule` | Resistance | 抗性 | 无（当前对应位置没有同类型 Tag） | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `variantrule` | 临时生命值 | 临时生命值 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/小鸟; 向镜中看.json` | `creature` | 人类定身术 | 人类定身术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `collection/小鸟; 向镜中看.json` | `creature` | 命令术 | 命令术 | 无（当前对应位置没有同类型 Tag） | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `condition` | 吸血鬼 | 吸血鬼 | 无（当前对应位置没有同类型 Tag） | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `condition` | 平民 | 平民 | 无（当前对应位置没有同类型 Tag） | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | 魅惑 | 魅惑 | 无（当前对应位置没有同类型 Tag） | 2 |
| `creature/Kobold Press; 万兽图志 2.json` | `skill` | 失能 | 失能 | 无（当前对应位置没有同类型 Tag） | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `skill` | 燃烧之手 | 燃烧之手 | 无（当前对应位置没有同类型 Tag） | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `condition` | 2d6 | 2d6 | 无（当前对应位置没有同类型 Tag） | 1 |
| `creature/MCDM Productions; 凡人，快逃！.json` | `creature` | 失能 | 失能 | 无（当前对应位置没有同类型 Tag） | 1 |
| `item/Giffyglyph; 奥术宝珠.json` | `condition` | deafened | 耳聋 | 无（当前对应位置没有同类型 Tag） | 1 |

## 译名或名称变化（不算删除）

| 文件 | 类型 | Tag 英文名 | 基线中文 Tag | 当前中文 Tag | 次数 |
|---|---|---|---|---|---:|
| `adventure/Kobold Press; 万兽图志2巢穴.json` | `condition` | unconscious | 无意识 | 昏迷 | 1 |
| `adventure/Kobold Press; 万兽图志2巢穴.json` | `creature` | carnivorous sod | 食肉草皮 | 肉食草皮 | 2 |
| `adventure/Kobold Press; 万兽图志2巢穴.json` | `skill` | Acrobatics | 杂技 | 特技 | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `condition` | Surprised | 惊讶 | 突袭 | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `creature` | Bjarki (Little Bear) | 比亚基（小熊） | 比亚基 | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `creature` | Odri'vetr | 奥德里维特 | 青年白龙 | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `creature` | Snati (Sniffer) | 斯纳提（嗅嗅） | 斯纳提 | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `creature` | Swarm of Sluaghs | 斯卢阿群 | 堕灵集群 | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `creature` | Tosti (Stout) | 托斯提（壮壮） | 托斯提 | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `creature` | Trollkin Reaver | 巨魔劫掠者 | 巨魔掠夺者 | 3 |
| `adventure/Kobold Press; 北地萨迦.json` | `deity` | The Bear Maiden | 熊少女 | 本格塔 | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `hazard` | Extreme Cold | 极端寒冷 | 极度寒冷 | 5 |
| `adventure/Kobold Press; 北地萨迦.json` | `item` | Cook's Utensils | 厨具 | 厨师工具 | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `skill` | Persuasion | 说服 | 游说 | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `table` | Travel Pace | 旅行步速 | 旅行步调 | 4 |
| `adventure/Kobold Press; 北地萨迦.json` | `variantrule` | Advantage | 死亡豁免 | 死亡豁免检定 | 1 |
| `adventure/Kobold Press; 北地萨迦.json` | `variantrule` | Cone [Area of Effect] | 锥形 [效应区域] | 锥状 [效应区域] | 2 |
| `adventure/Kobold Press; 北地萨迦.json` | `variantrule` | Death Saving Throw | 死亡豁免 | 死亡豁免检定 | 3 |
| `adventure/Kobold Press; 北地萨迦.json` | `variantrule` | Dim Light | 微光 | 微光光照 | 1 |
| `adventure/Kobold Press; 邪术师巢穴50：梅莫里亚之光.json` | `condition` | frightened | 恐惧 | 恐慌 | 1 |
| `adventure/Kobold Press; 邪术师巢穴50：梅莫里亚之光.json` | `item` | Map or Scroll Case | 地图或卷轴盒 | 地图或卷轴匣 | 1 |
| `adventure/Kobold Press; 邪术师巢穴50：梅莫里亚之光.json` | `item` | Spell Scroll (2nd Level) | 法术卷轴（2环） | 法术卷轴 | 1 |
| `adventure/Kobold Press; 邪术师巢穴50：梅莫里亚之光.json` | `item` | Spell Scroll (3rd Level) | 法术卷轴（3环） | 法术卷轴 | 1 |
| `adventure/Loot Tavern; 日与影之血.json` | `skill` | Persuasion | 说服 | 游说 | 3 |
| `adventure/Michael Galvis; 魔宠的困境.json` | `creature` | gremishka | 诡灵什卡 | 小法妖 | 12 |
| `adventure/Poison Potion Press; 梦想之滨.json` | `creature` | merrow | 迈罗人鱼 | 梅洛 | 1 |
| `adventure/Poison Potion Press; 梦想之滨.json` | `trap` | poison needle | 毒针 | 毒针陷阱 | 1 |
| `adventure/The Aciduous Adventurer; 弗里茨·冯·维尔格的奇妙机械宅邸.json` | `hazard` | Extreme Heat | 极端酷热 | 极度高温 | 1 |
| `adventure/The Aciduous Adventurer; 弗里茨·冯·维尔格的奇妙机械宅邸.json` | `item` | Sending Stones | 传讯石 | 短讯石 | 1 |
| `adventure/The Aciduous Adventurer; 弗里茨·冯·维尔格的奇妙机械宅邸.json` | `item` | Spell Scroll (2nd Level) | 法术卷轴（2环） | 法术卷轴 | 1 |
| `adventure/The Aciduous Adventurer; 弗里茨·冯·维尔格的奇妙机械宅邸.json` | `skill` | Intelligence | 智力 | 调查 | 2 |
| `adventure/TragicMissile; 无辜者的献祭.json` | `item` | Horde Sword | 部落之剑 | Horde Sword | 1 |
| `adventure/TragicMissile; 无辜者的献祭.json` | `skill` | 体操 | 体操 | Acrobatics | 1 |
| `adventure/TragicMissile; 无辜者的献祭.json` | `skill` | 生存 | 生存 | Survival | 3 |
| `adventure/TragicMissile; 无辜者的献祭.json` | `skill` | 说服 | 说服 | Persuasion | 1 |
| `adventure/Wyatt Trull; 疯法师的地城伴侣书 - 完整版.json` | `creature` | Gray Ooze (Psychic) | Gray Ooze (Psychic) | Gray Ooze | 1 |
| `book/2CGaming; 团灭怪物图鉴 - 第一卷.json` | `creature` | hill giant | 丘陵巨人 | 山丘巨人 | 1 |
| `book/Curio Solus; 节日活动.json` | `skill` | Survival Check | 生存 | 求生 | 1 |
| `book/Dave Eisinger; 识货商人的价格指南.json` | `item` | Emerald Pen | 祖母绿钢笔 | 翡翠钢笔 | 2 |
| `book/Dungeon Rollers; 先祖武器.json` | `condition` | blinding | blinding | 目盲 | 1 |
| `book/MCDM Productions; 阿卡迪亚 第27期.json` | `classFeature` | Mystic Connection | Mystic Connection | 秘术师联系 | 1 |
| `book/MCDM Productions; 阿卡迪亚 第27期.json` | `creature` | merrow | 迈罗人鱼 | 梅洛 | 1 |
| `book/MCDM Productions; 阿卡迪亚 第27期.json` | `optfeature` | Drag Them (4 Ferocity) | 拖走他们（4狂怒） | 拖拽他们（4狂怒） | 1 |
| `book/MCDM Productions; 阿卡迪亚 第3期.json` | `race` | Tiefling (Variant; Winged) | Tiefling (Variant; Winged) | Variant; Winged | 1 |
| `book/MCDM Productions; 阿卡迪亚 第7期.json` | `creature` | Night Hag (Coven) | 夜鬼婆（鬼婆集会） | 夜鬼婆 | 1 |
| `book/Wizards of the Coast; 冒险者联盟第四季：黑暗赠礼.json` | `classFeature` | turn undead | 驱散亡灵 | 引导神力：驱散不死生物 | 1 |
| `book/grzart; 鞑契异界传送指南.json` | `race` | Goblin | 地精 | 象族 | 1 |
| `book/ukyo; 魔法束缚纹身.json` | `spell` | Cure Light Wounds | 治疗轻伤 | 疗伤术 | 1 |
| `class/Benjamin Huffman; 拳斗士Pugilist - 2024.json` | `subclassFeature` | Dread Hand | 惧恶之手 | 恐惧之手 | 1 |
| `class/Benjamin Huffman; 魔战士Magus.json` | `spell` | arcing arrow | 电弧箭 | 弧光箭 | 1 |
| `class/Benjamin Huffman; 魔战士Magus.json` | `spell` | aspir | 汲魔术 | 夺能 | 1 |
| `class/Benjamin Huffman; 魔战士Magus.json` | `spell` | bloodletting bite | 放血撕咬 | 放血咬 | 1 |
| `class/Benjamin Huffman; 魔战士Magus.json` | `spell` | death shroud | 死亡裹布 | 死亡之罩 | 1 |
| `class/Benjamin Huffman; 魔战士Magus.json` | `spell` | drain | 汲取术 | 汲取 | 1 |
| `class/Benjamin Huffman; 魔战士Magus.json` | `spell` | rime strike | 霜击 | 霜寒打击 | 1 |
| `class/Benjamin Huffman; 魔战士Magus.json` | `spell` | warden's rebuke | 守卫惩戒 | 守卫者斥责 | 1 |
| `class/CaelReader; 优雅德鲁伊.json` | `spell` | acit rain | acit rain | 强酸雨 | 1 |
| `class/CaelReader; 优雅德鲁伊.json` | `spell` | blue | blue | 虹光法墙 | 1 |
| `class/CaelReader; 优雅德鲁伊.json` | `spell` | cause feat | cause feat | 造成恐惧 | 1 |
| `class/CaelReader; 优雅德鲁伊.json` | `spell` | guardians of nature | guardians of nature | 自然守卫 | 1 |
| `class/CaelReader; 优雅德鲁伊.json` | `spell` | stride | stride | 树跃术 | 1 |
| `class/Dan_UwU; 舞者.json` | `item` | ententeiner's pack | ententeiner's pack | Entertainer's Pack | 1 |
| `class/Dusk Zargoth; 游荡者重制版.json` | `item` | alchemist's fire | 炽火胶 | 炽火胶(扁瓶装) | 1 |
| `class/Eric Nell; 瘟疫医生.json` | `item` | Darts (30) | 飞镖(30) | 飞镖 | 1 |
| `class/Fragsauce; 缚魂者（重制版）.json` | `variantrule` | Create Your Companion page | 创造你的同伴页面 | 创造你的同伴 | 1 |
| `class/Ghostfire Gaming; 怪物猎人.json` | `background` | Outlander | Outlander | 化外之民 | 1 |
| `class/J.R. Raffles; 幽魂.json` | `condition` | conscious | 清醒 | 昏迷 | 1 |
| `class/KibblesTasty; 发明家.json` | `spell` | freezing shell | freezing shell | 冰冻外壳 | 3 |
| `class/KibblesTasty; 法剑士.json` | `spell` | pressure cutter | 压力切割器 | 高压水刀 | 1 |
| `class/KibblesTasty; 灵能使.json` | `optfeature` | discipline of Psychokinesis | discipline of Psychokinesis | 心灵念动学科 | 1 |
| `class/KibblesTasty; 灵能使.json` | `spell` | ice spike | 寒冰穿刺 | 寒冰尖刺 | 1 |
| `class/KibblesTasty; 灵能使.json` | `spell` | orbital stones | 轨道石 | 环绕飞石 | 1 |
| `class/KibblesTasty; 神秘学者.json` | `spell` | orbital stones | 轨道石 | 环绕飞石 | 1 |
| `class/KibblesTasty; 神秘学者.json` | `spell` | prismatic flash | 虹彩闪光 | 虹光闪耀 | 2 |
| `class/LaserLlama; 替代圣武士.json` | `spell` | conjure fiend (alternate) | 咒唤邪魔（变体） | 咒唤邪魔 | 1 |
| `class/LaserLlama; 替代血猎手.json` | `background` | Haunted One | 噩梦缠身 | 噩梦缠身者 | 1 |
| `class/LaserLlama; 萨满.json` | `spell` | restoration | 复原术 | 恢复术 | 1 |
| `class/MCDM Productions; 天赋者与灵能.json` | `item` | Orb of Psionic Might | 灵能伟力法球 | 灵能伟力法球+1 | 1 |
| `class/MCDM Productions; 野兽之心与怪物同伴.json` | `book` | upcoming monster book | 怪物书 | 凡人，快逃！ | 1 |
| `class/MCDM Productions; 野兽之心与怪物同伴.json` | `optfeature` | Brimstone Teleport | 硫磺传送 | 硫磺传送（8狂怒） | 1 |
| `class/MCDM Productions; 野兽之心与怪物同伴.json` | `optfeature` | Chains from Hell | 炼狱之锁链 | 炼狱之锁链（8狂怒） | 1 |
| `class/MCDM Productions; 野兽之心与怪物同伴.json` | `optfeature` | Dark of Hell | 地狱黑暗 | 地狱黑暗（8狂怒） | 1 |
| `class/MCDM Productions; 野兽之心与怪物同伴.json` | `optfeature` | Infernal Flames | 炼狱之焰 | 炼狱之焰（8狂怒） | 1 |
| `class/MCDM Productions; 野兽之心与怪物同伴.json` | `optfeature` | Lava Geyser | 熔岩间歇泉 | 熔岩间歇泉（8狂怒） | 1 |
| `class/MCDM Productions; 野兽之心与怪物同伴.json` | `optfeature` | Lightning Eruption | 闪电喷发 | 闪电喷发（8狂怒） | 1 |
| `class/MCDM Productions; 野兽之心与怪物同伴.json` | `optfeature` | Plant Prison | 植物囚笼 | 植物囚笼（5狂怒） | 1 |
| `class/MCDM Productions; 野兽之心与怪物同伴.json` | `optfeature` | Poison Rain | 毒雨 | 毒雨（8狂怒） | 1 |
| `class/MCDM Productions; 野兽之心与怪物同伴.json` | `optfeature` | Stinging Swarm | 蜇刺虫群 | 蜇刺虫群（6狂怒） | 1 |
| `class/MCDM Productions; 野兽之心与怪物同伴.json` | `optfeature` | Thunderous Rebuke | 雷霆反击 | 雷霆反击（6狂怒） | 1 |
| `class/Sam Grierson; 厨师The Cook Class.json` | `item` | crossbow bolts (20) | 弩矢（20） | 弩矢(20) | 1 |
| `class/Sam Grierson; 厨师The Cook Class.json` | `spell` | 变巨 | 变巨 | 变巨/缩小术 | 1 |
| `collection/1985 Games; 胧忆岛：矢田门物语.json` | `creature` | Jumaga | 朱玛加 | 天空蝾螈朱玛加 | 2 |
| `collection/1985 Games; 胧忆岛：矢田门物语.json` | `item` | Bundle of Peeping Willow | 窥视柳树捆 | 窥视柳树 | 1 |
| `collection/1985 Games; 胧忆岛：矢田门物语.json` | `subclass` | Coven | 集会宗主 | 集会 | 1 |
| `collection/1985 Games; 胧忆岛：矢田门物语.json` | `subclass` | Delivery | 递送之誓 | 递送 | 1 |
| `collection/1985 Games; 胧忆岛：矢田门物语.json` | `subclass` | Fortune | 命运游荡者 | 命运 | 1 |
| `collection/1985 Games; 胧忆岛：蒿野物语.json` | `creature` | merrow | 迈罗人鱼 | 梅洛 | 1 |
| `collection/Amellwind; 怪物猎人怪物图鉴.json` | `book` | Tasha's Cauldron for Everything rules (p.142) | 《塔莎的万事坩埚》规则（第142页） | 塔莎的万事坩埚 | 1 |
| `collection/Anthony Turco; 柯兰堡文摘：冒险者年鉴.json` | `creature` | tsoreva | tsoreva | 索雷瓦 | 1 |
| `collection/Anthony Turco; 柯兰堡文摘：冒险者年鉴.json` | `spell` | regeneration | regeneration | 再生术 | 1 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `class` | druid | druid | 德鲁伊 | 1 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `class` | fighter | fighter | 战士 | 2 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `class` | monk | monk | 武僧 | 1 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `class` | psion | psion | 灵能使 | 1 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `class` | rogue | rogue | 游荡者 | 1 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `skill` | Acrobatics | 杂技 | 特技 | 3 |
| `collection/Anthony Turco; 柯兰堡文摘：灵能使入门.json` | `skill` | Survival | 生存 | 求生 | 1 |
| `collection/Arcana Games; 阿卡迪亚.json` | `race` | Phaedran (Centaur) | 斐德兰人（人马） | 斐德兰人 | 1 |
| `collection/Arcana Games; 阿卡迪亚.json` | `race` | Phaedran (Gorgon) | 斐德兰人（戈耳工） | 斐德兰人 | 1 |
| `collection/Arcana Games; 阿卡迪亚.json` | `race` | Phaedran (Harpy) | 斐德兰人（鸟妖） | 斐德兰人 | 1 |
| `collection/Arcana Games; 阿卡迪亚.json` | `race` | Phaedran (Satyr) | 斐德兰人（半羊人） | 斐德兰人 | 1 |
| `collection/Arcana Games; 阿卡迪亚.json` | `race` | Phaedran (Siren) | 斐德兰人（塞壬） | 斐德兰人 | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | Ghast | 妖鬼 | 幽影 | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | Ghoul | 食尸鬼 | 木乃伊 | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | Polar Bear | 白熊 | 北极熊 | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | Randall Graham | 信鸽鬼婆 | 兰德尔·格雷厄姆 | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | Shadow | 幽影 | 丧尸 | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | Specter | 恶灵 | 尸妖 | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | The Barrow King | 巴罗国王的 | 巴罗国王 | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | The Grinning Sinner | 兰德尔·格雷厄姆 | 狞笑罪人 | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | Vermin Familiar (Centipede) | 害虫魔宠（蜈蚣） | 害兽魔宠 | 4 |
| `collection/Avantris; 歪曲之月.json` | `creature` | Vermin Familiar (Pigeon) | 害虫魔宠（鸽子） | 害兽魔宠 | 3 |
| `collection/Avantris; 歪曲之月.json` | `creature` | Vermin Familiar (Weasel) | 害虫魔宠（鼬鼠） | 害兽魔宠 | 3 |
| `collection/Avantris; 歪曲之月.json` | `creature` | Vessla Browntooth | 维斯拉 | 维斯拉·棕牙 | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | Wayward Haint | 幽影 | 迷途祟魂 | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | Zombie | 丧尸 | 鬼火 | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 害虫魔宠（鸽子） | 害虫魔宠（鸽子） | 害兽魔宠 | 5 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 戈索斯 | 戈索斯 | 枯朽之兽 | 2 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 拉乌姆 | 拉乌姆 | 丰收之怖 | 2 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 约格林 | 约格林 | 链之收割者 | 1 |
| `collection/Avantris; 歪曲之月.json` | `creature` | 蜘蛛集群 | 蜘蛛集群 | 蜘蛛群 | 1 |
| `collection/Avantris; 歪曲之月.json` | `item` | Amulet | 护身符 | 护符 | 2 |
| `collection/Avantris; 歪曲之月.json` | `item` | Chain | 链之魔契 | 链条 | 1 |
| `collection/Avantris; 歪曲之月.json` | `item` | Figurine of Wondrous Power, Silver Raven | 异能塑像，白银渡鸦 | 异能塑像, 白银渡鸦 | 1 |
| `collection/Avantris; 歪曲之月.json` | `item` | Musket | 滑膛枪 | 火铳 | 4 |
| `collection/Avantris; 歪曲之月.json` | `item` | Oil (flask) | 燃油(扁瓶装) | 燃油 (扁瓶) | 4 |
| `collection/Avantris; 歪曲之月.json` | `item` | Perfume (vial) | 香水(小瓶装) | 香水 (小瓶) | 1 |
| `collection/Avantris; 歪曲之月.json` | `reward` | Thread of Rejuvenation | 复苏之线 | 重生之线 | 4 |
| `collection/Avantris; 歪曲之月.json` | `skill` | Survival | 生存 | 求生 | 3 |
| `collection/Avantris; 歪曲之月.json` | `spell` | Darkness | 黑暗 | 黑暗术 | 9 |
| `collection/Avantris; 歪曲之月.json` | `spell` | Resistance | 抗性 | 抵抗术 | 2 |
| `collection/Avantris; 歪曲之月.json` | `spell` | Scrying | 探知 | 探知术 | 13 |
| `collection/Avantris; 歪曲之月.json` | `spell` | 探知 | 探知 | 探知术 | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `creature` | Hobgoblin Devastator | 大地精毁灭者 | 大地精破坏者 | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `race` | Dwarf (Ember) | 矮人（余烬） | 矮人 (余烬) | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `race` | Dwarf (Stone) | 矮人（岩石） | 矮人 (岩石) | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `race` | Dwarf (Tundra) | 矮人（冻原） | 矮人 (冻原) | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `race` | Elf (Bright) | 精灵（光耀） | 精灵 (光耀) | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `race` | Elf (Green) | 精灵（翠绿） | 精灵 (翠绿) | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `race` | Elf (Thimble) | 精灵（顶针） | 精灵 (顶针) | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `race` | Genasi (Ash) | 元素裔（灰烬） | 元素裔 (灰烬) | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `race` | Genasi (Ice) | 元素裔（冰） | 元素裔 (冰) | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `race` | Genasi (Slime) | 元素裔（软泥） | 元素裔 (软泥) | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `race` | Genasi (Storm) | 元素裔（风暴） | 元素裔 (风暴) | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `race` | Halfling (Jungle) | 半身人（丛林） | 半身人 (丛林) | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `race` | Halfling (River) | 半身人（河流） | 半身人 (河流) | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `race` | dwarf (ember) | 矮人（余烬） | 矮人 (余烬) | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `race` | dwarf (stone) | 矮人（岩石） | 矮人 (岩石) | 2 |
| `collection/Benevolent Evil; 元素与彼界.json` | `race` | elf (bright) | 精灵（光耀） | 精灵 (光耀) | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `race` | elf (green) | 精灵（翠绿） | 精灵 (翠绿) | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `race` | elf (thimble) | 精灵（顶针） | 精灵 (顶针) | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `race` | halfling (jungle) | 半身人（丛林） | 半身人 (丛林) | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | Frozen flame bomb, | 冻焰法球， | 冻焰法球 | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | Lightspeed haste, | 光速加速术， | 光速加速术 | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | Needle shower, | 针雨， | 针雨 | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | Scorching Rays | Scorching Rays | 灼热射线 | 2 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | Sword Burst | Sword Burst | 剑刃爆发 | 3 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | Twinkle toes, | 闪烁足尖， | 闪烁足尖 | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | aniamte dead | aniamte dead | animate dead | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | jolting weapon, | 震击武器， | 震击武器 | 1 |
| `collection/Benevolent Evil; 元素与彼界.json` | `spell` | lance of light, | 光之长枪， | 光之长枪 | 1 |
| `collection/Black Pudding Press; 海马露营者的完全食谱.json` | `item` | Dasher-staff of Imagination | Dasher-staff of Imagination | 想象餐具 | 1 |
| `collection/Black Pudding Press; 海马露营者的完全食谱.json` | `item` | Flour Sieve of Imagination | Flour Sieve of Imagination | 想象餐具 | 1 |
| `collection/Black Pudding Press; 海马露营者的完全食谱.json` | `item` | Kitchen Twine of Imagination | Kitchen Twine of Imagination | 想象餐具 | 1 |
| `collection/Black Pudding Press; 海马露营者的完全食谱.json` | `item` | Ladle of Imagination | Ladle of Imagination | 想象餐具 | 1 |
| `collection/Black Pudding Press; 海马露营者的完全食谱.json` | `item` | Measuring Spoons of Imagination | Measuring Spoons of Imagination | 想象餐具 | 1 |
| `collection/Black Pudding Press; 海马露营者的完全食谱.json` | `item` | Nutcracker of Imagination | Nutcracker of Imagination | 想象餐具 | 1 |
| `collection/Black Pudding Press; 海马露营者的完全食谱.json` | `item` | Pots & Pans Plate of Imagination | Pots & Pans Plate of Imagination | 想象餐具 | 1 |
| `collection/Black Pudding Press; 海马露营者的完全食谱.json` | `item` | Rolling Pin of Imagination | Rolling Pin of Imagination | 想象餐具 | 1 |
| `collection/Black Pudding Press; 海马露营者的完全食谱.json` | `item` | Saucebot of Imagination | Saucebot of Imagination | 想象餐具 | 1 |
| `collection/Black Pudding Press; 海马露营者的完全食谱.json` | `item` | Scales of Imagination | Scales of Imagination | 想象餐具 | 1 |
| `collection/Black Pudding Press; 海马露营者的完全食谱.json` | `item` | Skillet of Imagination | Skillet of Imagination | 想象餐具 | 1 |
| `collection/Black Pudding Press; 海马露营者的完全食谱.json` | `item` | Tongs of Imagination | Tongs of Imagination | 想象餐具 | 1 |
| `collection/Black Pudding Press; 海马露营者的完全食谱.json` | `item` | Wooden Spoon of Imagination | Wooden Spoon of Imagination | 想象餐具 | 1 |
| `collection/Black Pudding Press; 海马露营者的完全食谱.json` | `item` | Wooden Sword of Imagination | Wooden Sword of Imagination | 想象餐具 | 1 |
| `collection/Black Pudding Press; 海马露营者的完全食谱.json` | `spell` | dimesion door | dimesion door | Dimension Door | 1 |
| `collection/Bonus Action; 附赠动作.json` | `race` | genasi (fire) | genasi (fire) | 元素裔 | 1 |
| `collection/Darrington Press; 塔尔多雷战役设定集重制版.json` | `action` | cast a spell | 施法 | 施展法术 | 1 |
| `collection/Darrington Press; 塔尔多雷战役设定集重制版.json` | `creature` | diseased grick | 生病的穴居攫怪 | 染病穴居攫怪 | 7 |
| `collection/Darrington Press; 塔尔多雷战役设定集重制版.json` | `creature` | hippogriff | 鹫马 | 骏鹰 | 1 |
| `collection/Darrington Press; 塔尔多雷战役设定集重制版.json` | `creature` | merrow | 迈罗人鱼 | 梅洛 | 1 |
| `collection/Darrington Press; 塔尔多雷战役设定集重制版.json` | `item` | +1 weapon | +1武器 | +1 武器 | 1 |
| `collection/Darrington Press; 塔尔多雷战役设定集重制版.json` | `item` | gold (gp) | 金（gp） | 金币(gp) | 1 |
| `collection/Darrington Press; 塔尔多雷战役设定集重制版.json` | `item` | musket | 滑膛枪 | 火铳 | 2 |
| `collection/Darrington Press; 塔尔多雷战役设定集重制版.json` | `spell` | Healing Word | 治疗词 | 治愈真言 | 2 |
| `collection/DianaDM; 群星系列.json` | `creature` | ice giant | 冰巨人 | 霜巨人 | 1 |
| `collection/Echidna Design; 嘎嘎死灵书.json` | `creature` | Giant Goose Steed (Anserath) | 巨鹅坐骑（安瑟拉斯） | 巨鹅 | 1 |
| `collection/Echidna Design; 嘎嘎死灵书.json` | `creature` | Giant Goose Steed (Great Golden Goose) | 巨鹅坐骑（大金鹅） | 巨鹅 | 2 |
| `collection/Echidna Design; 嘎嘎死灵书.json` | `creature` | Giant Goose Steed (Ur-goose) | 巨鹅坐骑（始祖鹅） | 巨鹅 | 1 |
| `collection/Echidna Design; 嘎嘎死灵书.json` | `creature` | Goose Spirit (Honking Defender) | 鹅灵（嘎叫守卫） | 鹅灵 | 3 |
| `collection/Emperror; 恩佩罗的新节奏.json` | `item` | ersatz eye | 义眼 | Ersatz Eye | 1 |
| `collection/Emperror; 恩佩罗的新节奏.json` | `item` | mythallar | 迷锁能核 | 伊瑟琳城迷锁能核 | 2 |
| `collection/Emperror; 恩佩罗的新节奏.json` | `item` | tanglefoot bag | tanglefoot bag | 拌足袋 | 1 |
| `collection/Emperror; 恩佩罗的新节奏.json` | `spell` | snare | 圈套术 | Snare | 1 |
| `collection/Frog God Games; 拉潘·阿图克 2018.json` | `item` | gold dragon scale mail | 金龙鳞甲 | Dragon Scale Mail | 1 |
| `collection/Frog God Games; 拉潘·阿图克 2018.json` | `item` | ring of protection | 防护戒指 | Ring of Protection | 2 |
| `collection/Frog God Games; 拉潘·阿图克 2018.json` | `variantrule` | Damage | 伤害 | Damage | 1 |
| `collection/Frog God Games; 拉潘·阿图克 2018.json` | `variantrule` | Possession | 附身 | Possession | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `book` | spore servant | 孢子奴仆 | 孢子仆从模板 | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `condition` | deafened | 耳聋 | 魅惑 | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `optfeature` | Pact of the Brand | Pact of the Brand | 烙印 | 12 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `spell` | Tenser's Destructive Disc | Tenser's Destructive Disc | 谭森毁灭浮碟 | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `spell` | acid arrow | 强酸箭 | 马友夫强酸箭 | 1 |
| `collection/FungusAmongUs; 亚比达奇的可憎冒险者.json` | `spell` | blindness/deafeness | blindness/deafeness | 目盲术/耳聋术 | 1 |
| `collection/Genuine Fantasy Press; 被遗忘的秘密合集：觉醒.json` | `creature` | wealth mimic | 财富拟身怪 | 财富拟身怪（凯伦西） | 2 |
| `collection/Ghostfire Gaming; 塞巴斯蒂安·克劳的德拉肯海姆指南.json` | `item` | shield | 护盾术 | 盾牌 | 4 |
| `collection/Ghostfire Gaming; 塞巴斯蒂安·克劳的德拉肯海姆指南.json` | `spell` | light | 轻型 | 光亮术 | 1 |
| `collection/Ghostfire Gaming; 塞巴斯蒂安·克劳的德拉肯海姆指南.json` | `spell` | scrying | 探知 | 探知术 | 3 |
| `collection/Ghostfire Gaming; 塞巴斯蒂安·克劳的德拉肯海姆指南.json` | `spell` | spirit guardian | 先祖守卫 | 灵体卫士 | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆之墟.json` | `creature` | merrow | 迈罗人鱼 | 梅洛 | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆之墟.json` | `skill` | Survival | 生存 | 求生 | 10 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `action` | study | 研究 | 搜索 | 12 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `creature` | Eldritch Crawler | 诡秘爬行者 | 骇异惧蛛 | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `creature` | Walking Delerium Geode | 行走晶洞 | 行走的谵妄石英簇 | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `creature` | 鼠怪 | 鼠怪 | 老鼠 | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `item` | Spell Scroll (Cantrip) | 法术卷轴（戏法） | 法术卷轴 | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | Arcana | 洞悉 | 求生 | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | Arcana | 洞悉 | 自然 | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | Arcana | 自然 | 医药 | 2 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | History | 宗教 | 历史 | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | History | 自然 | 历史 | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | Medicine | 求生 | 洞悉 | 2 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | Nature | 医药 | 求生 | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `skill` | Survival | 医药 | 自然 | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | Resistance | 抗性 | 抵抗术 | 5 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | Scrying | 探知术 鬼婆可以将其真菌法杖或粘液球攻击替换为以下效果： | 探知术 | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | Shield | 盾牌 | 护盾术 | 2 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `spell` | nondetection | nontection | 回避侦测 | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `variantrule` | Hit Points | 先攻 | 生命值 | 1 |
| `collection/Ghostfire Gaming; 德拉肯海姆的怪物.json` | `variantrule` | Immunity | 抗性 | 免疫 | 1 |
| `collection/Ghostfire Gaming; 鬼魅幽谷 - 玩家指南 - 2024.json` | `creature` | Wraith | 狂怒 | 邪灵 | 1 |
| `collection/Ghostfire Gaming; 鬼魅幽谷 - 玩家指南 - 2024.json` | `creature` | 老鼠群 | 老鼠群 | 鼠群 | 1 |
| `collection/Ghostfire Gaming; 鬼魅幽谷 - 玩家指南 - 2024.json` | `feat` | Advanced Weapon Proficiency (FS) | 高级武器熟练 | 高级武器熟练 (FS) | 1 |
| `collection/Ghostfire Gaming; 鬼魅幽谷 - 玩家指南 - 2024.json` | `feat` | Advanced Weapon Proficiency (G) | 高级武器熟练 | 高级武器熟练（G） | 1 |
| `collection/Ghostfire Gaming; 鬼魅幽谷 - 玩家指南 - 2024.json` | `item` | Breath of Beleth | 贝莱特之息 | 贝莱特之息（毒素） | 1 |
| `collection/Ghostfire Gaming; 鬼魅幽谷 - 玩家指南 - 2024.json` | `optfeature` | Magical Savvy | 魔法大师 | 魔法精通 | 1 |
| `collection/Ghostfire Gaming; 鬼魅幽谷 - 玩家指南 - 2024.json` | `spell` | Scrying | 探知 | 探知术 | 2 |
| `collection/Ghostfire Gaming; 鬼魅幽谷 - 玩家指南 - 2024.json` | `spell` | Slow | 缓速 | 缓慢术 | 1 |
| `collection/Ghostfire Gaming; 鬼魅幽谷 - 玩家指南 - 2024.json` | `spell` | Summon Plant | 召唤植物 | 召唤植物精魄 | 1 |
| `collection/Ghostfire Gaming; 鬼魅幽谷 - 玩家指南 - 2024.json` | `spell` | 黑暗 | 黑暗 | 黑暗术 | 1 |
| `collection/Ghostfire Gaming; 鬼魅幽谷 - 玩家指南 - 2024.json` | `subclass` | Fractured | 破碎者 | 破碎 | 1 |
| `collection/Griffin Macaulay; 狮鹫的鞍中珍宝Ⅱ.json` | `creature` | Hippogriff | 鹫马 | 骏鹰 | 1 |
| `collection/Griffin Macaulay; 狮鹫的鞍中珍宝Ⅱ.json` | `creature` | gelatinous cube | 胶质方块 | 凝胶方块 | 2 |
| `collection/Griffin Macaulay; 狮鹫的鞍中珍宝Ⅱ.json` | `creature` | merrow | 迈罗人鱼 | 梅洛 | 1 |
| `collection/Griffin Macaulay; 狮鹫的鞍中珍宝Ⅱ.json` | `item` | +3 longbow | +3长弓 | 长弓 | 1 |
| `collection/Griffin Macaulay; 狮鹫的鞍中珍宝Ⅱ.json` | `item` | ale (gallon) | 麦芽酒（加仑） | 麦酒（加仑） | 1 |
| `collection/Griffin Macaulay; 狮鹫的鞍中珍宝Ⅱ.json` | `item` | hide barding | 表皮具装 | 兽皮甲 | 1 |
| `collection/Griffin Macaulay; 狮鹫的鞍中珍宝Ⅱ.json` | `item` | shield | 护盾术 | 盾牌 | 4 |
| `collection/Griffin Macaulay; 狮鹫的鞍中珍宝Ⅱ.json` | `spell` | Scrying | 探知 | 探知术 | 1 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `adventure` | Cloud of Emberbats | 余烬蝙蝠群 | 接近林地 | 1 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `adventure` | If Odwald was apprehended | 如果奥德瓦尔德被捕获 | 奥德瓦尔德的命运 | 1 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `creature` | ashsnake | 火焰之面 | 烈焰之相 | 1 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `creature` | ashsnake | 灰蛇 | 灰烬蛇 | 4 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `creature` | aspect of fire | 火焰之面 | 烈焰之相 | 5 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `creature` | aspect of fire | 灰蛇 | 灰烬蛇 | 1 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `creature` | caustic slime | 腐蚀性史莱姆 | 腐蚀史莱姆 | 9 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `creature` | forest prowler | 森林潜行者 | 森林潜猎兽 | 3 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `creature` | lesser demon | 小恶魔 | 次级恶魔 | 1 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `creature` | mountain lion | 山地狮 | 山狮 | 3 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `creature` | shifting slime | 变化的粘液 | 变形史莱姆 | 4 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `creature` | sticky slime | 变化的粘液 | 变形史莱姆 | 1 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `creature` | strig knight | 斯特里骑士 | 鸮族骑士 | 3 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `creature` | swarm of emberbats | 一群余烬蝙蝠 | 火烬蝠集群 | 6 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `item` | figurine of wondrous power, silver raven | 奇物雕像，白银渡鸦 | 异能塑像, 白银渡鸦 | 1 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `item` | quiver | 弩矢（20） | 弩矢(20) | 1 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `language` | Giant Eagle | 巨鹰 | 巨鹰语 | 1 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `language` | Giant Elk | 巨赤鹿 | 巨赤鹿语 | 1 |
| `collection/Hit Point Press; 谦卑林战役设定集.json` | `language` | Giant Owl | 巨猫头鹰 | 巨猫头鹰语 | 1 |
| `collection/Hit Point Press; 谦卑林故事集.json` | `creature` | Lorno Burrowbright | 骄傲之喾 | 洛诺·伯罗布赖特 | 7 |
| `collection/Hit Point Press; 谦卑林故事集.json` | `creature` | Raptor Deckhand (Net Gun) | 隼族甲板水手（捕网枪） | 隼族甲板水手 | 1 |
| `collection/Hit Point Press; 谦卑林故事集.json` | `creature` | Saltfeather | 骄傲之喾 | 洛诺·伯罗布赖特 | 1 |
| `collection/Hit Point Press; 谦卑林故事集.json` | `creature` | panther | 黑豹 | 豹 | 1 |
| `collection/Hit Point Press; 谦卑林故事集.json` | `item` | Kwark's wondrous kernels | 夸克的奇妙内核，可投掷内核 | 夸克的奇妙内核，可投掷 | 1 |
| `collection/Hit Point Press; 谦卑林故事集.json` | `item` | Kwark's wondrous kernels | 夸克的奇妙内核，播种者内核 | 夸克的奇妙内核，种植者 | 1 |
| `collection/Hit Point Press; 谦卑林故事集.json` | `item` | Oil (flask) | 燃油(扁瓶装) | 燃油 (扁瓶) | 1 |
| `collection/Hit Point Press; 谦卑林故事集.json` | `item` | Ring of X-ray vision | X光视野戒指 | X射线戒指 | 1 |
| `collection/James Ohlen; 博德之门的英雄们.json` | `creature` | 游荡剑客 | 游荡剑客 | 剑客 | 1 |
| `collection/James Ohlen; 博德之门的英雄们.json` | `item` | 真理血清 | 真理血清 | 吐真剂 | 1 |
| `collection/James Ohlen; 博德之门的英雄们.json` | `skill` | 生存 | 生存 | 求生 | 2 |
| `collection/James Ohlen; 博德之门的英雄们.json` | `spell` | 元素咒唤术 | 元素咒唤术 | 咒唤元素 | 1 |
| `collection/James Ohlen; 博德之门的英雄们.json` | `spell` | 动物咒唤术 | 动物咒唤术 | 咒唤兽群 | 2 |
| `collection/James Ohlen; 博德之门的英雄们.json` | `spell` | 次级元素咒唤术 | 次级元素咒唤术 | 咒唤微元素群 | 1 |
| `collection/James Ohlen; 博德之门的英雄们.json` | `spell` | 次级复原术 | 次级复原术 | 次等复原术 | 1 |
| `collection/James Ohlen; 博德之门的英雄们.json` | `spell` | 毒气喷溅 | 毒气喷溅 | 毒气喷涌 | 4 |
| `collection/James Ohlen; 博德之门的英雄们.json` | `spell` | 野兽知觉 | 野兽知觉 | 野兽感官 | 2 |
| `collection/James Ohlen; 博德之门的英雄们.json` | `spell` | 魅惑人类 | 魅惑人类 | 魅惑类人 | 1 |
| `collection/Kobold Press; 北地世界书.json` | `creature` | Hraesvelgr | 赫瑞斯维尔格 | 哈斯维格 | 3 |
| `collection/Kobold Press; 北地世界书.json` | `creature` | Liosalfar | 光精灵 | 莉莎尔法 | 1 |
| `collection/Kobold Press; 北地世界书.json` | `creature` | Red Hag | 红鬼婆 | 红巫婆 | 1 |
| `collection/Kobold Press; 北地世界书.json` | `creature` | Trollkin Berserker | 巨魔裔狂战士 | 巨魔狂战士 | 1 |
| `collection/Kobold Press; 北地世界书.json` | `spell` | Bone-Chilling Smite | 彻骨斩 | 烈焰攻城 | 1 |
| `collection/Kobold Press; 北地世界书.json` | `spell` | Call to Action | 号令行动 | 彻骨斩 | 1 |
| `collection/Kobold Press; 北地世界书.json` | `spell` | Freyja's Grace | 弗蕾雅的恩典 | 号令行动 | 1 |
| `collection/Kobold Press; 北地世界书.json` | `spell` | Reaver's Rune | 劫掠者符文 | 希芙的恩典 | 1 |
| `collection/Kobold Press; 北地世界书.json` | `spell` | Shield-Maiden's Favor | 盾女的眷顾 | 劫掠者符文 | 1 |
| `collection/Kobold Press; 北地世界书.json` | `spell` | Sif's Grace | 希芙的恩典 | 高贵牺牲 | 1 |
| `collection/Kobold Press; 北地世界书.json` | `spell` | Trickster's Bluff | 诡计者的虚张声势 | 女武神的视界 | 1 |
| `collection/Kobold Press; 北地世界书.json` | `spell` | Truth's Blade | 真相之刃 | 玄命的棋子 | 1 |
| `collection/Kobold Press; 北地世界书.json` | `spell` | Valkyrie's Guidance | 女武神的指引 | 盾墙之歌 | 1 |
| `collection/Kobold Press; 北地世界书.json` | `spell` | Valkyrie's Vision | 女武神的视界 | 真相之刃 | 1 |
| `collection/Kobold Press; 北地世界书.json` | `subclass` | Fenris | 芬里斯结社 | 芬里斯 | 1 |
| `collection/Kobold Press; 北地世界书.json` | `subclass` | Titan | 泰坦之道 | 泰坦 | 1 |
| `collection/Kobold Press; 北地世界书.json` | `subclass` | Valhalla | 瓦尔哈拉誓约 | 瓦尔哈拉 | 1 |
| `collection/Kobold Press; 北地世界书.json` | `table` | Raiding Target | 劫掠目标 | 劫掠目标（抽象） | 2 |
| `collection/Kobold Press; 北地世界书.json` | `variantrule` | Weapon Mastery Properties | 武器精通特性 | 武器精通词条 | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `book` | Tome of Beasts | 万兽图志 | 万兽图志1（2023版） | 3 |
| `collection/Kobold Press; 黯潮之书.json` | `book` | Tome of Beasts 1 | 万兽图册1 | 万兽图志1（2023版） | 94 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Algorith | 算法龙 | 算律者 | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Black Knight Commander | 黑骑士指挥官 | 黑骑士长 | 2 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Chained Angel | 锁链天使 | 锁缚天使 | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | City Watch Captain | 城市守卫队长 | 城邦护卫队长 | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Devilbound Gnome | 恶魔契约侏儒 | 魔契侏儒 | 2 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Domovoi | 多莫沃伊 | 护宅妖 | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Drowned Maiden | 溺水少女 | 溺亡少女 | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Dwarven ringmage | 矮人环法师 | 矮人法环术师 | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Elvish Veteran Archer | 精灵老练弓箭手 | 精灵百战弓手 | 2 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Emerald Order Cult Leader | 翡翠秩序邪教首领 | 翠玉邪教首脑 | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Fext | 费克斯 | 尸巫 | 3 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Gearforged Templar | 机械锻造圣堂武士 | 锻俑圣堂武士 | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Hippogriff | 鹫马 | 骏鹰 | 2 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Living Wick | 活灯芯 | 活化烛芯 | 2 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Merrow | 迈罗人鱼 | 梅洛 | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Panther | 黑豹 | 豹 | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Psoglav Demon | Psoglav 恶魔 | 狗头魔 | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Sandman | 沙人 | 睡魔 | 2 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Skein Witch | 丝织女巫 | 缠纱魔女 | 2 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Slow Storm | 慢风暴 | 迟滞风暴 | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Swarm of Sluaghs | 软泥怪群 | 堕灵集群 | 5 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Wolf Reaver Dwarf | 狼骑矮人 | 矮人狼掠者 | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | Xhkarsh | Xhkarsh（克萨尔什） | 克萨尔什 | 2 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | city watch captain | 城市守卫队长 | 城邦护卫队长 | 3 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | domovoi | 多莫沃伊 | 护宅妖 | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | dwarven ringmage | 矮人环法师 | 矮人法环术师 | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `creature` | wolf reaver dwarf | 狼骑矮人 | 矮人狼掠者 | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `race` | Darakhul (Bearfolk Heritage) | 达拉库食尸鬼（熊民传承） | 达拉库食尸鬼 (熊民遗承) | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `race` | Darakhul (Shadow Goblin Heritage) | 达拉库食尸鬼（暗影哥布林传承） | 达拉库食尸鬼 (幽影地精遗承) | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `race` | Elf (Lunar) | 精灵 (月) | 精灵 (月之术法) | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `race` | Elf (Sable) | 精灵 (暗) | 精灵 (黑色) | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `race` | Satarre (Unbound) | 萨塔雷（未绑定） | 萨塔雷 (不羁) | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `race` | Shade (Stygian) | 幽影（冥河） | 幽影 (冥河) | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `race` | Umbral Human (Changeling) | 影蚀人类（幻身灵） | 影蚀人类 (幻身灵) | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `race` | Umbral Human (Gifted) | 影蚀人类（天赋者） | 影蚀人类 (天赋者) | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `spell` | Lesser restoration | 次级复原术 | 次等复原术 | 1 |
| `collection/Kobold Press; 黯潮之书.json` | `spell` | lesser restoration | 次级复原术 | 次等复原术 | 7 |
| `collection/Scichopath; 寂静挽歌.json` | `variantrule` |  |  | 冷漠【态度】 | 1 |
| `collection/Scichopath; 寂静挽歌.json` | `variantrule` |  |  | 友好【态度】 | 1 |
| `collection/Scichopath; 寂静挽歌.json` | `variantrule` |  |  | 敌对【态度】 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `condition` | invisible | 隐形 | 目盲 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `condition` | prone | 倒地 | 目盲 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | Bigby's hand | 毕格比之手 | 变身术 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | Evard's black tentacles | 艾伐黑触手 | 自然守卫 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | abeyed discharge | abeyed discharge | 延迟放电 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | arcane eye | 秘法眼 | 英雄宴 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | banishing smite | 放逐斩 | 祝福术 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | bestow blessing | bestow blessing | 授福 | 3 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | bestow curse | 降咒 | 咒唤兽群 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | bestow malediction | bestow malediction | 降祸 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | bless | 祝福术 | 脆弱诅咒 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | blindness/deafness | 目盲术/耳聋术 | 寻获魔宠 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | blink | 闪现术 | 混沌武器 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | cause fear | 造成恐惧 | 匕首之云 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | cause fear | 造成恐惧 | 吸血鬼之触 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | chaos bolt | 混乱箭 | 脆弱诅咒 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | chaos weapon | chaos weapon | 混沌武器 | 5 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | commune | 通神术 | 地狱呼唤 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | counterspell | 法术反制 | 强化属性 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | create bog | create bog | 造沼 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | crown of madness | 疯狂冠冕 | 次等复原术 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | detect past | detect past | 侦测过去 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | disguise self | 易容术 | 毕格比之手 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | dispel caster | dispel caster | 解除施法者 | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | dragon's breath | 龙息术 | 变形术 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | duel of destiny | duel of destiny | 命运决斗 | 3 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | dusk | 黄昏 | 暮色 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | elemental spike | elemental spike | 元素尖刺 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | embrace destiny | 拥抱宿命 | 拥抱命运 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | enhance ability | 强化属性 | 疯狂冠冕 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | enhance ability | 强化属性 | 闪电束 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | faerie fire | 妖火 | 睡眠术 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | find familiar | 寻获魔宠 | 迷踪步 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | find familiar | 寻获魔宠 | 魔法飞弹 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | find vessel | find vessel | 寻获船只 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | fire bolt | 火焰箭 | 德鲁伊伎俩 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | fortuity conflux | fortuity conflux | 机运汇流 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | guardian of faith | 信仰守卫 | 艾伐黑触手 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | guiding bolt | 光导箭 | 变形术 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | guiding weapon | guiding weapon | 导引武器 | 6 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | healing word | 治愈真言 | 七彩喷射 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | heroes' feast | 英雄宴 | 安定心神 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | hex | 脆弱诅咒 | 纠缠术 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | infernal calling | 地狱呼唤 | 启蒙术 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | invisible weapon | invisible weapon | 无形武器 | 5 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | last rites | 安灵仪式 | 临终圣礼 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | light | 光亮术 | 火焰箭 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | mage barrier | mage barrier | 法师屏障 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | magic missile | 魔法飞弹 | 易容术 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | misty step | 迷踪步 | 侦测魔法 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | oath-sealing covenant | 誓约封印 | 封誓圣约 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | oscillating chronology | oscillating chronology | 振荡岁月 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | part and parcel | part and parcel | 寄递包裹 | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | polymorph | 变形术 | 龙息术 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | primordial weapon | primordial weapon | 原初武器 | 7 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | quarry's mark | quarry's mark | 猎物标记 | 3 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | raise dead | 死者复活 | 妖火 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | ray of frost | 冷冻射线 | 根须陷阱 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | reaping smite | reaping smite | 收割圣斩 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | remove curse | 移除诅咒 | 降咒 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | sacred flame | 圣火术 | 冷冻射线 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | shadow blade | 幽影刃 | 行动无踪 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | shoulder cannon | shoulder cannon | 肩炮 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | skull servant | skull servant | 骷髅仆从 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | sleep | 睡眠术 | 异怪召唤术 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | stolen life | stolen life | 窃取生命 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | subdue beast | subdue beast | 驯服野兽 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | sundering smite | 破击猛击 | 崩解圣斩 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | tale of hope & woe | tale of hope & woe | 希望与哀伤的故事 | 2 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | thaumaturgy | 奇术 | 荆棘之鞭 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | throat rend | throat rend | 撕裂咽喉 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | vampiric weapon | vampiric weapon | 吸血武器 | 6 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | ward against weapons | ward against weapons | 御兵防护 | 1 |
| `collection/Sterling Vermin Adventuring Co.; 终极冒险者手册.json` | `spell` | wish | 祈愿术 | 幽影刃 | 1 |
| `collection/小鸟; 向镜中看.json` | `variantrule` | 敌对 [态度] | 敌对 [态度] | 敌对【态度】 | 2 |
| `creature/Kobold Press; 万兽图志 2.json` | `condition` | grappled | 擒抱 | 受擒 | 2 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | Poena, Duke of Retribution | Poena，复仇公爵 | 惩罚公爵波伊娜 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | alehouse drake | 酒馆龙兽 | 酒馆幼龙 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | animated object (small) | 活化物件（小型） | 活化物体(小型) | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | avatar of boreas | 玻瑞阿斯的化身 | 北风之神化身 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | clurichaun | 克鲁瑞坎 | 克鲁查恩 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | commoner | 这个 | 平民 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | death butterfly swarm | 死亡蝴蝶 | 死亡蝴蝶群 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | elder shadow drake | 上古幽影龙兽 | 老暗影龙 | 3 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | gelatinous cube | 胶质方块 | 凝胶方块 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | hippogriff | 鹫马 | 骏鹰 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | lorelei | 罗蕾莱 | 洛蕾莱 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | mammon, archduke of greed | 玛门，贪婪的大公 | 玛门，贪婪大公 | 2 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | mechuiti, demon lord of apes | 梅奎提，猿之恶魔领主 | 猿之恶魔领主梅丘提 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | miremal | 米雷马尔 | 泥沼兽 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | nyctli | 尼科力 | 尼克特利 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | orphan of the black | 漆黑遗孤 | 黑裔孤儿 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | polar bear | 白熊 | 北极熊 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | ratfolk | 鼠人 | 鼠族 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | repository | 知识库 | 资源库 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | rum gremlin | 朗姆地精 | 朗姆酒地精 | 5 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | sea dragon wyrmling | 海龙雏龙 | 海龙幼龙 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | spider of leng | 冷原蜘蛛 | 冷之蜘蛛 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `creature` | wampus cat | wampus猫 | 沃姆帕斯猫 | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `item` | Holy Water (flask) | 圣水(扁瓶装) | 圣水 (扁瓶) | 1 |
| `creature/Kobold Press; 万兽图志 2.json` | `item` | ball bearings (bag of 1,000) | 滚珠（一袋1000颗） | 滚珠 (一袋1,000粒) | 2 |
| `creature/Kobold Press; 万兽图志 2.json` | `item` | holy water (flask) | 圣水(扁瓶装) | 圣水 (扁瓶) | 2 |
| `creature/Kobold Press; 万兽图志 2.json` | `item` | shield | 护盾术 | 盾牌 | 8 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | ala | ala | 阿拉 | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | gray orc | 灰色兽人 | 灰兽人 | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | star thrall | 沙子鬼婆 | 沙地巫婆 | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | subek | subek | 苏贝克 | 2 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | 冰元素生物 | 冰元素生物 | 冰元素 | 3 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | 吞噬巨兽 | 吞噬巨兽 | 巨噬兽 | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | 大师巫妖 | 大师巫妖 | 艺术大师巫妖 | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | 巨人蚁 | 巨人蚁 | 巨型蚁 | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | 幽魂骑士 | 幽魂骑士 | 幽灵骑士 | 2 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | 恐惧行者隧道挖掘 | 恐惧行者隧道挖掘 | 惧行挖掘者 | 2 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | 携带者蚊 | 携带者蚊 | 携带者蚊子 | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | 暮萎蕈人 | 暮萎蕈人 | 死亡帽菌类生物 | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | 朗姆地精 | 朗姆地精 | 朗姆酒地精 | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | 水晶独石 | 水晶独石 | 水晶巨碑 | 2 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | 沙飘龙兽 | 沙飘龙兽 | 流沙龙兽 | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | 瑟希尔巨人 | 瑟希尔巨人 | 瑟西尔巨人 | 3 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | 白熊 | 白熊 | 北极熊 | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | 矿物泥怪 | 矿物泥怪 | 矿物软泥 | 2 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | 胶质方块 | 胶质方块 | 凝胶方块 | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | 艾琳娜 | 艾琳娜 | 伊阿拉 | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `creature` | 首领鱼 | 首领鱼 | 阿尔法鱼 | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `item` | acid (vial) | 强酸（小瓶） | 强酸 (小瓶) | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `item` | shield | 护盾术 | 盾牌 | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `item` | 护盾术 | 护盾术 | 盾牌 | 7 |
| `creature/Kobold Press; 万兽图志 3.json` | `item` | 炽火胶（扁瓶） | 炽火胶（扁瓶） | 炽火胶(扁瓶装) | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `item` | 神奇法力雕像，大理石象 | 神奇法力雕像，大理石象 | 异能塑像，大理石象 | 1 |
| `creature/Kobold Press; 万兽图志 3.json` | `language` | Orc | 兽人 | 兽人语 | 2 |
| `creature/Kobold Press; 万兽图志 3.json` | `race` | 提夫林（伊奥文西亚夫） | 提夫林（伊奥文西亚夫） | 提夫林 | 1 |
| `creature/Kobold Press; 万兽图志.json` | `item` | shield | 护盾术 | 盾牌 | 11 |
| `creature/Kobold Press; 万兽图志.json` | `spell` | arms of hadar | 护甲 | 法师护甲 | 1 |
| `creature/Kobold Press; 万兽图志.json` | `spell` | lesser restoration | 次级复原术 | 次等复原术 | 17 |
| `creature/Kobold Press; 万兽图志1（2023版）.json` | `creature` | spinosaurus dinosaur | 棘龙 | 棘龙恐龙 | 1 |
| `creature/Kobold Press; 万兽图志1（2023版）.json` | `item` | shield | 护盾术 | 盾牌 | 10 |
| `creature/Kobold Press; 万兽图志1（2023版）.json` | `spell` | lesser restoration | 次级复原术 | 次等复原术 | 6 |
| `creature/LaserLlama; 野兽合集.json` | `condition` | Frightened | 恐惧 | 恐慌 | 7 |
| `creature/LaserLlama; 野兽合集.json` | `creature` | mule | 骡子 | Mule | 1 |
| `creature/LaserLlama; 野兽合集.json` | `creature` | ox | 公牛 | Ox | 1 |
| `creature/LaserLlama; 野兽合集.json` | `spell` | conjure familiar | 召唤魔宠 | 咒唤魔宠 | 4 |
| `creature/MCDM Productions; 凡人，快逃！.json` | `creature` | gnoll abyssal archer | 豺狼人深渊射手 | 鬣狗人深渊射手 | 1 |
| `creature/MCDM Productions; 凡人，快逃！.json` | `item` | iron bands of Bilarro | 绑定铁索 | 比拉罗的铁索 | 1 |
| `creature/MCDM Productions; 凡人，快逃！.json` | `item` | shield | 护盾术 | 盾牌 | 27 |
| `creature/MCDM Productions; 凡人，快逃！.json` | `spell` | Nystul's magic aura | 奥术师魔法灵光 | 涅斯图魔法灵光 | 1 |
| `creature/MCDM Productions; 凡人，快逃！.json` | `spell` | lesser restoration | 次级复原术 | 次等复原术 | 14 |
| `item/Giffyglyph; 奥术宝珠.json` | `item` | +1 Longbow | +1 Longbow | +1 长弓 | 1 |
