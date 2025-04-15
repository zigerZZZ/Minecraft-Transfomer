# 仓库说明

一个使用预训练Transformer微调的Minecraft机翻模型

*微调没有对一些特殊字符做任何处理*

## 如何使用

```
pip install -r requirements.txt
python translator.py
```

具体使用方法可以参考`translator.py`

- 如果需要更快的翻译速度，请安装gpu版本的torch和cuda

## 数据来源

参考我的另一个仓库[Minecraft-Moded-Language-Dataset](https://github.com/zigerZZZ/Minecraft-Moded-Language-Dataset)

## 模型训练

该模型在上述数据集共计50w条数据上训练了12轮，使用`NVDIA A40`显卡，训练6小时

## 文件说明

`datas\`存放数据集的文件夹

`fine-tuned-model\`存放微调模型的文件夹

`MyDataset.py`一个torch的Dataset类

`train.py`训练入口

`translator.py`翻译示例

## 运行示例
```
原文: Minecraft
机翻: Minecraft

原文: Botania
机翻: 植物魔法

原文: chest
机翻: 箱子

原文: cobblestone
机翻: 圆石

原文: mob
机翻: 生物

原文: mob spawner
机翻: 生物刷怪笼

原文: Cupronickel Coil Block
机翻: 白铜线圈方块

原文: vanilla Minecraft
机翻: 原版Minecraft

--------------------
原文: Rainbow Curry
译文: 彩虹咖喱
机翻: 彩色咖喱

原文: Diorite Tiles
译文: 闪长岩瓦
机翻: 闪长岩瓦

原文: Copper to Iron Upgrade
译文: 铜->铁升级
机翻: 铜→铁升级

原文: Down-Gate Cactus Light Gray Terracotta Timber Frame
译文: 下门形仙人掌淡灰色陶瓦木制框架
机翻: 下门形仙人掌淡灰色陶瓦木制框架

原文: WAAAGH!
译文: 哇!
机翻: WAAAGH!

原文: Flint Clay
译文: 石粘土
机翻: 燧石粘土

原文: Small Pile of Invar Dust
译文: 小堆殷钢粉
机翻: 小堆殷钢粉

原文: Hunter Module: Looting II
译文: 猎人模块:抢夺 II
机翻: 猎杀模块：抢夺 II

原文: Fires a dart in the direction you are pointing which damages and weakens its target.
译文: 向你所指向的方向发射飞镖,造成伤害并削弱目标。
机翻: 向你指的方向发射飞镖，造成伤害并使目标获得虚弱II效果。

原文: Crossed Jungle Brown Terracotta Timber Frame
译文: 十字丛林木棕色陶瓦木制框架
机翻: 十字丛林木棕色陶瓦木制框架
```

## TOD

- 发布机翻桌面软件：输入整合包路径即可对`.snbt`和`en_us.json`进行翻译
