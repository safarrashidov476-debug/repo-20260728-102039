import sys

path = sys.argv[1]
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

changed = False

# 1) onProgressDownload - progress e'lon qilish + maydon qo'shish + tugaganda tovush
old_download = """    @Override
    public void onProgressDownload(String fileName, long downloadedSize, long totalSize) {
        float progress = totalSize == 0 ? 0 : Math.min(1f, downloadedSize / (float) totalSize);
        currentMessageObject.loadedFileSize = downloadedSize;
        createLoadingProgressLayout(downloadedSize, totalSize);"""

new_download = """    private int lastAnnouncedProgressPercent = -1;

    @Override
    public void onProgressDownload(String fileName, long downloadedSize, long totalSize) {
        float progress = totalSize == 0 ? 0 : Math.min(1f, downloadedSize / (float) totalSize);
        currentMessageObject.loadedFileSize = downloadedSize;
        createLoadingProgressLayout(downloadedSize, totalSize);
        int accPercentDown = (int) (progress * 100);
        if (accPercentDown - lastAnnouncedProgressPercent >= 10 || accPercentDown == 100) {
            lastAnnouncedProgressPercent = accPercentDown;
            sendAccessibilityEventForVirtualView(MessageAccessibilityNodeProvider.HOST_VIEW_ID, AccessibilityEvent.TYPE_ANNOUNCEMENT, accPercentDown + " foiz yuklab olindi");
            if (accPercentDown == 100) {
                try {
                    android.media.ToneGenerator accDownloadDoneTone = new android.media.ToneGenerator(android.media.AudioManager.STREAM_NOTIFICATION, 100);
                    accDownloadDoneTone.startTone(android.media.ToneGenerator.TONE_PROP_BEEP2, 250);
                } catch (Exception accToneError) {
                    // tovushni chalib bo'lmasa, e'lon qilish baribir ishlayveradi
                }
            }
        }"""

if old_download in content:
    content = content.replace(old_download, new_download, 1)
    changed = True
    print("onProgressDownload - progress e'lon qilish + tugash tovushi qo'shildi")
else:
    print("OGOHLANTIRISH: onProgressDownload bloki topilmadi, o'tkazib yuborildi")

# 2) onProgressUpload - progress e'lon qilish
old_upload = """    @Override
    public void onProgressUpload(String fileName, long uploadedSize, long totalSize, boolean isEncrypted) {
        float progress = totalSize == 0 ? 0 : Math.min(1f, uploadedSize / (float) totalSize);
        currentMessageObject.loadedFileSize = uploadedSize;
        radialProgress.setProgress(progress, true);"""

new_upload = """    @Override
    public void onProgressUpload(String fileName, long uploadedSize, long totalSize, boolean isEncrypted) {
        float progress = totalSize == 0 ? 0 : Math.min(1f, uploadedSize / (float) totalSize);
        currentMessageObject.loadedFileSize = uploadedSize;
        radialProgress.setProgress(progress, true);
        int accPercentUp = (int) (progress * 100);
        if (accPercentUp - lastAnnouncedProgressPercent >= 10 || accPercentUp == 100) {
            lastAnnouncedProgressPercent = accPercentUp;
            sendAccessibilityEventForVirtualView(MessageAccessibilityNodeProvider.HOST_VIEW_ID, AccessibilityEvent.TYPE_ANNOUNCEMENT, accPercentUp + " foiz jo'natildi");
        }"""

if old_upload in content:
    content = content.replace(old_upload, new_upload, 1)
    changed = True
    print("onProgressUpload - progress e'lon qilish qo'shildi")
else:
    print("OGOHLANTIRISH: onProgressUpload bloki topilmadi, o'tkazib yuborildi")

if changed:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
