import { Injectable, Param } from '@nestjs/common';
import {
  CreateTextMessageRequestDto,
  TextMessageDto,
} from 'src/types/text-message.dto';
import * as admin from 'firebase-admin';
import { log } from 'console';

@Injectable()
export class TextMessagesService {
  constructor() {}

  async findById(id: string): Promise<TextMessageDto> {
    const firestore = admin.firestore();
    const collectionRef = firestore.collection('TextMessages');
    const documentRef = collectionRef.doc(id);
    const document = await documentRef.get();
    if (!document.exists) {
      console.log(`テキストメッセージ [${id}] が見つかりません`);
      return null;
    }

    const data = document.data();
    const message = TextMessageDto.createFromFirestoreData(id, data);
    return message;
  }

  async create(dto: CreateTextMessageRequestDto): Promise<TextMessageDto> {
    const firestore = admin.firestore();
    const collectionRef = firestore.collection('TextMessages');
    const documentRef = await collectionRef.add({
      ...dto,
      sendsAt: admin.firestore.FieldValue.serverTimestamp(),
    });
    const data = (await documentRef.get()).data();
    const message = TextMessageDto.createFromFirestoreData(
      documentRef.id,
      data,
    );
    return message;
  }

  async findAllId(): Promise<string[]> {
    const allMessages = [];

    const db = admin.firestore();
    const idRef = db.collection('TextMessages');
    const q = await idRef.orderBy('sendsAt', 'desc').get();
    q.forEach((document) => {
      console.log(document.id, '=>', document.data());
    });

    // const snapshot = await idRef.get();
    // snapshot.forEach((doc) => {
    //   doc.id, '=>', doc.data();
    // });

    // IDのみを取りだし、配列idに保存。ターミナル上で出力するとIDが表紙されるがブラウザで表示させると映らない(解決済み)
    // ↑原因:配列で返される関数をさらに配列にpushしていた
    // ターミナル上で表示されたのは一個手前の変数snapshotをlogで表示してたため
    // ここのIDを時間順に並び返す作業
    const id = q.docs.map((doc) => doc.id);

    // メッセージ全体を配列に保存(一応)
    allMessages.push(q);
    console.log(allMessages);

    // メモ：for文書き方
    // for (var i = 0; i < id.length; i++) {
    //   const ans = this.findById(id[i]);
    // }

    return id;
  }

  async findAllMessages(): Promise<string[]> {
    const db = admin.firestore();
    const allMessagesRef = db.collection('TextMessages');
    const all = await allMessagesRef.orderBy('sendsAt', 'desc').get();
    const allMessages = [];
    all.forEach((doc) => {
      allMessages.push(doc.id, '=>', doc.data());
    });

    return allMessages;
  }
}
