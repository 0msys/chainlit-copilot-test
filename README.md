# このリポジトリについて

このリポジトリは、ChainlitのCopilot機能をReactに埋め込む実験を行ったリポジトリです。
紹介は[こちらの記事](https://zenn.dev/0msys/articles/b820a5530a4073)にあります。
コンテナを使って起動することを想定しています。

こちらを使う前に、Docker desktop等のコンテナを使える環境を整えてください。


## 使い方

### アプリの起動

このリポジトリをクローンし、以下のコマンドを実行してください。

```bash
docker compose up -d
```

`localhost:3000`にアクセスすることで利用できます。

アプリにアクセスすると、Reactのチュートリアルにある三目並べのゲームが表示されます。

その右下に吹き出しのアイコンがありますので、そちらをクリックすると、ChainlitのチャットUIが表示されます。

チャットにメッセージを入力し、送信すると、三目並べの戦況が返信されます。

また、ブラウザのコンソールにチャットから送られたメッセージがログが出力されますので、ReactとChainlitの通信が行われていることが確認できます。

さらに、`localhost:8000`にアクセスすると、通常のChainlitアプリにアクセスできます。

こちらは通信相手のReactがいませんので当然戦況は表示されませんが、チャットのオウム返しは行われます。

アクセスしているアプリは同じですが、Copilotかどうかで挙動が変わることが確認できます。

### アプリの停止

以下のコマンドを実行してください。

```bash
docker compose down
```


## 参考

- [Reactのチュートリアル](https://ja.react.dev/learn/tutorial-tic-tac-toe)
- [ChainlitのCopilotドキュメント](https://docs.chainlit.io/deployment/copilot)