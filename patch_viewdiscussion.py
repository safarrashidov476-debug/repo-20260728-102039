import sys

path = sys.argv[1]
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

anchor = "options.add(OPTION_VIEW_REPLIES_OR_THREAD);"

new_block_after = """
                if (!isThreadChat() && chatMode != MODE_SCHEDULED && currentChat != null && ChatObject.isChannel(currentChat) && !currentChat.megagroup && currentChat.has_link && primaryMessage != null) {
                    items.add(LocaleController.getString(R.string.ViewDiscussion));
                    options.add(OPTION_VIEW_REPLIES_OR_THREAD);
                    icons.add(R.drawable.msg_viewreplies);
                }"""

count = content.count(anchor)
if count == 0:
    print("OGOHLANTIRISH: 'options.add(OPTION_VIEW_REPLIES_OR_THREAD);' topilmadi, patch o'tkazib yuborildi")
else:
    # Har bir uchragan joydan keyin (lekin faqat ASL uchraganlar, biz qo'shgan
    # yangilarini qayta ushlamaslik uchun avval hammasini indekslarini topamiz)
    pieces = content.split(anchor)
    rebuilt = pieces[0]
    for i in range(1, len(pieces)):
        rebuilt += anchor + new_block_after + pieces[i]
    content = rebuilt
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"ChatActivity.java - {count} ta joyga 'Muhokamani ko'rish' bandi qo'shildi")
