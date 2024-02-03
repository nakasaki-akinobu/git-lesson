# -*- coding: utf-8 -*-
"""kadai_017

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19D19JmZL0L9HsIXhuyQIWrBowJd_mS29
"""

# 名前(name)と年齢(age)の属性を持つHumanクラスを作成
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# check_adult メソッドを作成
  def check_adult(self):
    # ageが20以上の場合に大人であること
    if self.age >= 20:
      print("{}は大人です。".format(self.name))
# そうでない場合に大人でないこと
    else:
      print("{}は大人ではありません。".format(self.name))

# Humanクラスのインスタンスを複数生成リスト
human_data1 = Human("侍太郎", 36)
human_data2 = Human("侍一郎", 20)
human_data3 = Human("侍花子", 18)

# 上記をリストに追加
human_datum = ["human_data1", "human_data2", "human_data3"]

# リストの要素数分だけcheck_adultメソッドにアクセスして実行
human_data1.check_adult()