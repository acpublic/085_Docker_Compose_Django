// 現在の時刻を取得する関数
function getCurrentTime() {
    const now = new Date(); // 現在の日時を取得
    const hours = now.getHours().toString().padStart(2, '0'); // 時間 (2桁に補完)
    const minutes = now.getMinutes().toString().padStart(2, '0'); // 分 (2桁に補完)
    const seconds = now.getSeconds().toString().padStart(2, '0'); // 秒 (2桁に補完)
    return `${hours}:${minutes}:${seconds}`; // 時刻を "HH:MM:SS" の形式で返す
}

// 時刻をHTMLに表示する
function displayTime() {
    const timeElement = document.getElementById('currentTime');
    timeElement.textContent = getCurrentTime();
}

// ページが読み込まれたときに時刻を表示
window.onload = function () {
    //displayTime(); // 最初に表示
    setInterval(displayTime, 1000); // 1秒ごとに時刻を更新
};
