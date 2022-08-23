#Lambda環境変数
#RDSにも同様のタグを設定する
TAGKEY	AUTO_STOP
TAGVALUE	true

#EventBridge cron
#毎日23:30(JST)に実行
30 14 * * ? *