# iPOST

## システム構成

- Client
  - iPOST 本体
    - RaspberryPi
    - 老人宅に設置される
  - iPOST アプリ
    - スマートフォンアプリ
- Web Server
  - クラウド上の Web Server

## Web API

Web Server が Client に対して提供する API

- iPOST 本体
  - メッセージ（手書きの手紙の画像）を iPOST アプリへ送信する
    - POST
    - /machine/messages
  - iPOST アプリから送信されたメッセージの一覧を取得する
  - すべてのメッセージを取得
  - GET
  - /machine/messages/all
    - GET
    - /machine/messages
  - iPOST アプリから送信された個別のメッセージ（テキスト）を受信する
    - GET
    - /machine/messages/{id}
- iPOST アプリ
  - メッセージ（テキスト）を iPOST 本体へ送信する
    - POST
    - /mobile/messages
  - iPOST 本体から送信されたメッセージの一覧を取得する
    - GET
    - /mobile/messages
  - iPOST 本体から送信された個別のメッセージ（画像）を受信する
    - GET
    - /mobile/messages/{id}
  - iPOST アプリから送信されたメッセージの一覧を取得する
    - すべてのメッセージを取得
    - GET
    - /mobile/messages/all

## Web Server の機能

- Web API の提供
- 送信されたメッセージの保存
  - iPOST 本体からの画像メッセージ
  - iPOST アプリからのテキストメッセージ

## Web Server の構成

- HTTP Server
  - Google Cloud Platform
    - CloudRun
  - Framework
    - NestJS
      - TypeScript
- ストレージ
  - Google Cloud Platform
    - Cloud Storage
- データベース
  - Google Cloud Platform
    - Cloud fireStore

## メッセージ内容

### iPOST アプリから送信するテキストメッセージ

- メッセージ本文
- 送信者ID
- 送信者名

### Web Server で登録されたテキストメッセージ

送信されたテキストメッセージを Web Server 内のデータベースに保存する内容

- id
  - Web Server で付加
- 送信日時
  - Web Server で付加
- メッセージ本文
- 送信者ID
- 送信者名
