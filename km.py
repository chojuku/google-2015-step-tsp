# -*- coding: utf-8 -*-
import wx
import random
import math


class MyMainWindow(wx.Frame):
    def __init__(self, parent=None, id=-1, title=None):
        #フレームにパネルを設定
        wx.Frame.__init__(self, parent, id, title)
        self.panel = wx.Panel(self, size=(300, 300))
        self.panel.SetBackgroundColour('000000')
        self.Fit()
        #イベント
        self.panel.Bind(wx.EVT_PAINT, self.on_paint)
        self.panel.Bind(wx.EVT_LEFT_DOWN, self.on_left_click)
        self.panel.Bind(wx.EVT_RIGHT_DOWN, self.on_right_click)
        #変数初期化
        self.dots = []
        self.dc = None
        #クラスタは赤緑青の三種類
        self.cluster_types = ('#FF0000', '#00FF00', '#0000FF')
        self.clusters = [(0, 0), (0, 0), (0, 0)]
        #dotの初期セット
        self.shuffle_dots()

    def on_paint(self, event):
        u"""描画イベント"""
        self.dc = wx.PaintDC(self.panel)
        #マス目を書く
        self.dc.SetPen(wx.Pen('#CCCCCC', 1))
        for x in range(0, 300, 10):
            self.dc.DrawLine(x, 0, x, 300)
            for y in range(0, 300, 10):
                self.dc.DrawLine(0, y, 300, y)
            #dotを描画する
        for dot in self.dots:
            self.dc.SetPen(wx.Pen(self.cluster_types[dot['cluster']], 5))
            self.dc.DrawPoint(dot['x'], dot['y'])
            #クラスタの重心を描画する。
        self.draw_cluster()

    def on_left_click(self, evt):
        u"""左クリックでクラスタを再計算"""
        self.change_cluster()
        self.Refresh()

    def on_right_click(self, evt):
        u"""右クリックでdotをリセット"""
        self.shuffle_dots()
        self.Refresh()

    def shuffle_dots(self):
        u"""dotをランダムに配置する。"""
        self.dots = []
        for i in range(30):
            self.dots.append({'x': random.randint(0, 300),
                              'y': random.randint(0, 300),
                              'cluster': random.randint(0, len(self.cluster_types) - 1)})

    def draw_cluster(self):
        u"""クラスタを描画する。"""
        self.clusters = []
        for c in range(len(self.cluster_types)):
            #クラスタの重心＝クラスタに所属するdotの座標の平均
            self.dc.SetPen(wx.Pen(self.cluster_types[c], 1))
            count = sum(1 for dot in self.dots if dot['cluster'] == c)
            x = sum(dot['x'] for dot in self.dots if dot['cluster'] == c) // count if count != 0 else 150
            y = sum(dot['y'] for dot in self.dots if dot['cluster'] == c) // count if count != 0 else 150
            self.clusters.append({'x': x, 'y': y})
            #クラスタを×印で描画
            self.dc.DrawLine(x - 5, y - 5, x + 5, y + 5)
            self.dc.DrawLine(x + 5, y - 5, x - 5, y + 5)
            #クラスタから各dotまでを線で引く。
            self.dc.SetPen(wx.Pen(self.cluster_types[c], 0.8))
            for dot in self.dots:
                if dot['cluster'] == c:
                    self.dc.DrawLine(x, y, dot['x'], dot['y'])

    def change_cluster(self):
        u"""各dotの所属を最寄りのクラスタに変更する。"""
        for d in range(len(self.dots)):
            near_dist = 99999
            #二点間の距離＝√( (X1-X2)^2+(Y1-Y2)^2 )
            for c in range(len(self.cluster_types)):
                dist = math.sqrt(
                    (self.dots[d]['x'] - self.clusters[c]['x']) ** 2 + (self.dots[d]['y'] - self.clusters[c]['y']) ** 2)
                #一番最寄りのクラスタに鞍替え
                if near_dist >= dist:
                    self.dots[d]['cluster'] = c
                    near_dist = dist


if __name__ == '__main__':
    app = wx.PySimpleApp()
    w = MyMainWindow(title='K-Means Test')
    w.Center()
    w.Show()
    app.MainLoop()
