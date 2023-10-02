import * as admin from 'firebase-admin';

/**
 * スマホから送信されたメッセージを表すクラス
 * メッセージ本文はテキストである
 */
export class TextMessageDto {
  /**
   * メッセージID
   */
  id: string;

  /**
   * 送信日時
   */
  sendsAt: Date;

  /**
   * メッセージ文
   */
  text: string;

  /**
   * 送信者ID
   */
  senderId: string;

  /**
   * 送信者名
   */
  senderName: string;

  public static createFromFirestoreData(
    id: string,
    data: admin.firestore.DocumentData,
  ): TextMessageDto {
    const message = new TextMessageDto();
    message.id = id;
    message.text = data.text;
    message.senderId = data.senderId;
    message.senderName = data.senderName;
    message.sendsAt = new Date(data.sendsAt.seconds * 1000);
    return message;
  }
}

export class CreateTextMessageRequestDto {
  /**
   * メッセージ文
   */
  text: string;

  /**
   * 送信者ID
   */
  senderId: string;

  /**
   * 送信者名
   */
  senderName: string;
}
