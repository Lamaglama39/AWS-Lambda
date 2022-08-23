#Lambda環境変数
#RDSにも同様のタグを設定する
TAGKEY	AUTO_START
TAGVALUE	true

#EventBridge cron
#毎日08:00(JST)に実行
00 23 * * ? *