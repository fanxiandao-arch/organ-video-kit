# 素材索引（先读这个，再按 key 取用）

key 直接写进 episode.json；图片放 library/img/<key>.jpg，动图放 library/clips/<名>.mp4（用 `clip:<名>[@起始秒]`）。organ_video.py 先找 eps/<slug>/img，找不到自动用 library。

## 3D 动图 clips（约 6 秒，写实 3D）
| key | 内容 | 器官 |
|---|---|---|
| clip:liver1 | 肝小叶血流汇聚 | 肝 |
| clip:kid1 | 肾单位滤过与重吸收 | 肾 |
| clip:kid2 | 肾冠状剖面血流滤过 | 肾 |
| clip:lung1 | 肺泡簇呼吸鼓缩 | 肺 |

## 器官静态图
| key | 内容 | 风格 |
|---|---|---|
| liver_png | 肝与肝小叶锚点图 | 写实 3D |
| kid_png | 肾单位与肾小球锚点图 | 写实 3D |
| lung_hero / lung_alv / lung_bronchi | 整肺 / 肺泡 / 支气管树 | AI 玻璃 |
| u_hero / u_lining / u_contract / u_warn | 子宫全貌 / 内膜 / 收缩 / 警示红光 | AI 玻璃（玫瑰粉） |
| r_hero / r_hormone / r_tense / r_nodule | 乳腺腺叶 / 激素波动 / 紧绷 / 小结节 | AI 玻璃（玫瑰粉） |
| h_hero / h_rest / h_grow | 单个毛囊剖面 / 毛囊休止期 / 头发新生 | AI 玻璃（玫瑰粉） |

## 通用场景（每集可复用）
| key | 内容 |
|---|---|
| x_phone | 手机点赞收藏 |
| x_comment | 评论区互动 |
| x_ambulance | 救护车 / 120 |

## 生活场景
| key | 内容 |
|---|---|
| l_dinner / l_food / l_hangover / l_redface / l_sauna | 酒局 / 下酒菜 / 宿醉 / 喝酒脸红 / 酒后桑拿 |
| k_driver / k_meeting / k_mahjong / k_night / k_water / k_elder | 开车 / 开会 / 打麻将 / 夜尿 / 喝水 / 老人 |
| c_elder_cough / c_night / c_eating / c_patback / c_window | 老人咳嗽 / 夜咳 / 吃饭呛咳 / 拍背 / 开窗通风 |
| w_cramp / w_office / w_milktea / w_warm | 痛经蜷床 / 上班痛经 / 冰奶茶 / 热敷 |
| r_angry / r_sulk / r_walk / r_check | 办公室生气 / 夜里生闷气 / 散步放松 / 医院体检 |
| h_brush / h_overtime / h_drain / h_ponytail / h_sleep | 梳子掉发 / 熬夜加班 / 下水口头发 / 扎紧马尾 / 安稳睡觉 |

## 已做剧集（eps/<slug>/episode.json，可当模板）
| slug | 标题 | 配音 | 主题色 |
|---|---|---|---|
| liver_drink | 我是你的肝·喝酒篇 | 云健 | 默认金黄 |
| kidney_hold | 我是你的肾·憋尿篇 | 云健 | 默认金黄 |
| lung_cough | 我是你的肺·老人咳嗽篇 | 云健 | 默认金黄 |
| uterus_pain | 我是你的子宫·痛经篇（女性号首期；结尾互动已按新规改，成片是旧版） | 晓晓 | 玫瑰粉 |
| breast_anger | 我是你的乳腺·爱生气篇 | 晓晓 | 玫瑰粉 |
| hair_stress | 我是你的毛囊·压力掉发篇 | 晓晓 | 玫瑰粉 |

## 其他
- music/river_flows_in_you.mp3：爱给网来源，商用授权未确认。
- library/brand/：「她的身体说明书」头像 a2。
- 新增素材后，在对应表格加一行（key + 一句话内容）。
