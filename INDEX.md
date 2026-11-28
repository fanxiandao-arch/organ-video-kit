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
| p_hero / p_loose / p_contract | 盆底肌吊床托器官 / 吊床松弛下垂 / 收缩发光上提 | AI 玻璃（玫瑰粉） |
| v_hero / v_constrict / v_core | 手部血管网 / 指尖血管收缩发冷 / 热量留给心脑 | AI 玻璃（玫瑰粉） |
| t_hero / t_nodule / t_hormone | 蝴蝶形甲状腺 / 良性小结节 / 激素流向全身 | AI 玻璃（玫瑰粉） |
| ht_hero / ht_fast / ht_signal | 玻璃心脏 / 心跳加速光环 / 大脑发警报到心脏 | AI 玻璃（玫瑰粉） |
| g_hero / g_brain / g_cramp | 玻璃肠道 / 脑-肠神经连线 / 肠道痉挛 | AI 玻璃（玫瑰粉） |
| s_hero / s_barrier | 皮肤分层剖面 / 角质砖墙裂缝失水 |
| kn_hero / kn_cartilage / kn_muscle | 玻璃膝关节 / 软骨磨损裂纹 / 大腿肌肉护膝 |
| tr_hero / tr_mucus | 玻璃喉咙声带 / 黏液层干裂纤毛 |
| bl_hero / bl_signal | 玻璃泌尿系统 / 膀胱充盈发信号到大脑 |
| nk_hero / nk_forward | 玻璃颈椎七节 / 低头颈椎受压发红 |
| bn_hero / bn_porous | 玻璃股骨蜂窝骨小梁 / 骨小梁稀疏变空 | AI 玻璃（玫瑰粉） |

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
| p_newmom / p_sneeze / p_lift / p_situp / p_kegel | 新手妈妈夜里抱娃 / 产后打喷嚏 / 弯腰抱娃 / 产后仰卧起坐 / 仰躺放松练盆底 |
| v_coldhands / v_office / v_drink / v_footsoak / v_walk / v_diet / v_meal | 冬天街头哈手 / 办公室裹毯子 / 火锅喝酒脸红 / 泡脚 / 冬日快走 / 节食小沙拉 / 暖热家常饭 |
| t_report / t_ultrasound / t_mirror / t_salt / t_worry | 看体检报告 / 颈部B超 / 照镜摸脖子 / 碘盐海带紫菜 / 夜里看手机担心（人物像孕妇，非孕期题慎用） |
| ht_night / ht_coffee / ht_breath / ht_phone | 半夜惊醒捂胸口 / 深夜加班咖啡浓茶 / 床边闭眼慢呼吸 / 躺床刷手机焦虑 |
| g_exam / g_toilet / g_pills / g_breath | 上台前捂肚子紧张 / 走廊赶去厕所 / 桌上一堆药盒 / 沙发手放肚子慢呼吸 |
| s_heater / s_shower / s_scratch / s_scrub / s_lotion / s_humid | 暖气房挠手臂 / 热水澡蒸汽 / 夜里挠小腿白道 / 搓澡巾搓红 / 浴后抹润肤霜 / 卧室加湿器 |
| kn_cold / kn_stairs / kn_legraise / kn_sofa | 冬天露脚踝扶膝 / 爬楼梯扶膝 / 瑜伽垫直腿抬高 / 沙发窝着看电视 |
| tr_wake / tr_talk / tr_candy / tr_hotpot / tr_water / tr_mask | 暖气房半夜干醒摸喉咙 / 老师讲课嗓子哑 / 一堆润喉糖 / 辣火锅烫茶 / 双手捧温水 / 冬天戴口罩 |
| bl_night / bl_office / bl_water / bl_hold / bl_warm | 冬夜起床去厕所 / 开会中途离席 / 推开水杯不喝水 / 挤地铁憋尿 / 裹毯子穿厚袜保暖 |
| nk_phone / nk_desk / nk_pillow / nk_crack / nk_stretch | 地铁低头刷手机 / 电脑前揉脖子 / 高枕头睡觉 / 自己猛掰脖子 / 工位收下巴练习 |
| bn_sun / bn_milk / bn_soup / bn_fall / bn_hunch | 冬日公园晒太阳 / 奶豆腐绿叶菜早餐 / 油乎乎骨头汤 / 五十多岁女性冰面滑倒 / 五十多岁女性镜前驼背 |

## 已做剧集（eps/<slug>/episode.json，可当模板）
| slug | 标题 | 配音 | 主题色 |
|---|---|---|---|
| liver_drink | 我是你的肝·喝酒篇 | 云健 | 默认金黄 |
| kidney_hold | 我是你的肾·憋尿篇 | 云健 | 默认金黄 |
| lung_cough | 我是你的肺·老人咳嗽篇 | 云健 | 默认金黄 |
| uterus_pain | 我是你的子宫·痛经篇（女性号首期；结尾互动已按新规改，成片是旧版） | 晓晓 | 玫瑰粉 |
| breast_anger | 我是你的乳腺·爱生气篇 | 晓晓 | 玫瑰粉 |
| hair_stress | 我是你的毛囊·压力掉发篇 | 晓晓 | 玫瑰粉 |
| postpartum_pelvic | 我是你的盆底肌·产后松弛篇 | 晓晓 | 玫瑰粉 |
| cold_hands | 我是你的血管·冬天手脚冰凉篇 | 晓晓 | 玫瑰粉 |
| thyroid_nodule | 我是你的甲状腺·体检查出结节篇 | 晓晓 | 玫瑰粉 |
| heart_anxiety | 我是你的心脏·焦虑心慌篇 | 晓晓 | 玫瑰粉 |
| gut_nervous | 我是你的肠道·一紧张就肚子疼篇 | 晓晓 | 玫瑰粉 |
| skin_dry | 我是你的皮肤·冬天干痒篇 | 晓晓 | 玫瑰粉 |
| knee_cold | 我是你的膝盖·冬天一冷就酸疼篇 | 晓晓 | 玫瑰粉 |
| throat_dry | 我是你的喉咙·暖气房嗓子干疼篇 | 晓晓 | 玫瑰粉 |
| bladder_cold | 我是你的膀胱·冬天老想上厕所篇 | 晓晓 | 玫瑰粉 |
| neck_phone | 我是你的颈椎·低头刷手机篇（首次：13秒评论小花钩子 + 语速+15%） | 晓晓 | 玫瑰粉 |
| bone_winter | 我是你的骨头·冬天骨质疏松篇（同上） | 晓晓 | 玫瑰粉 |

## 已做选题（含不在本仓库的，选新题前先查）
- 肺、肝（喝酒）、肾、胃、毛囊、乳腺、子宫、卵巢、盆底肌、眼睛、食道（烫食）、跟腱/腱鞘、血管（手脚冰凉）、甲状腺（结节）、心脏（焦虑心慌）、肠道（一紧张就肚子疼）、皮肤（冬天干痒）、膝盖（冬天酸疼）、喉咙（暖气房干疼）、膀胱（冬天尿频）、颈椎（低头刷手机）、骨头（骨质疏松）

## 其他
- music/river_flows_in_you.mp3：爱给网来源，商用授权未确认。
- library/brand/：「她的身体说明书」头像 a2。
- 新增素材后，在对应表格加一行（key + 一句话内容）。
