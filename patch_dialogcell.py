import sys

path = sys.argv[1]
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old_block = """            } else if (user != null) {
                if (UserObject.isReplyUser(user)) {
                    sb.append(getString(R.string.RepliesTitle));
                } else if (UserObject.isAnonymous(user)) {
                    sb.append(getString(R.string.AnonymousForward));
                } else {
                    if (user.bot) {
                        sb.append(getString(R.string.Bot));
                        sb.append(". ");
                    }
                    if (user.self) {
                        sb.append(getString(R.string.SavedMessages));
                    } else {
                        sb.append(ContactsController.formatName(user.first_name, user.last_name));
                    }
                }
                sb.append(". ");
            } else if (chat != null) {
                if (chat.broadcast) {
                    sb.append(getString(R.string.AccDescrChannel));
                } else {
                    sb.append(getString(R.string.AccDescrGroup));
                }
                sb.append(". ");
                sb.append(chat.title);
                sb.append(". ");
            }"""

new_block = """            } else if (user != null) {
                if (UserObject.isReplyUser(user)) {
                    sb.append(getString(R.string.RepliesTitle));
                } else if (UserObject.isAnonymous(user)) {
                    sb.append(getString(R.string.AnonymousForward));
                } else {
                    if (user.self) {
                        sb.append(getString(R.string.SavedMessages));
                    } else {
                        sb.append(ContactsController.formatName(user.first_name, user.last_name));
                    }
                    if (user.bot) {
                        sb.append(". ");
                        sb.append(getString(R.string.Bot));
                    }
                }
                sb.append(". ");
            } else if (chat != null) {
                sb.append(chat.title);
                sb.append(". ");
                if (chat.broadcast) {
                    sb.append(getString(R.string.AccDescrChannel));
                } else {
                    sb.append(getString(R.string.AccDescrGroup));
                }
                sb.append(". ");
            }"""

if old_block not in content:
    print("OGOHLANTIRISH: DialogCell.java - eski blok topilmadi, bu patch o'tkazib yuborildi (Telegram manbasi o'zgargan bo'lishi mumkin)")
else:
    content = content.replace(old_block, new_block, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("DialogCell.java - nomlanish tartibi muvaffaqiyatli tuzatildi")
