import streamlit as st
import streamlit.components.v1 as components

# Cấu hình trang Streamlit
st.set_page_config(
    page_title="Đạp Xe Bình Yên - Peaceful Bike Ride",
    page_icon="🚲",
    layout="wide"
)

st.title("🚲 Đạp Xe Bình Yên (Peaceful Bike Ride)")
st.caption("Một không gian thư giãn: Đạp xe thong thả dưới hoàng hôn, ngắm mây bay và tận hưởng sự bình yên.")

# Hướng dẫn điều khiển nhẹ nhàng
with st.expander("📖 Hướng dẫn trải nghiệm", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        * **Đạp nhanh hơn:** Nhấn và giữ phím `D` hoặc phím mũi tên `Phải` ($\rightarrow$)
        * **Đi chậm/Thả trôi:** Nhấn và giữ phím `A` hoặc phím mũi tên `Trái` ($\leftarrow$)
        """)
    with col2:
        st.markdown("""
        * **Mục tiêu:** Không có áp lực thời gian hay kẻ địch nào cả. Chỉ cần đạp xe và tận hưởng khung cảnh!
        * **Gợi ý:** Hãy bật một bản nhạc nhẹ nhàng bên ngoài để tăng trải nghiệm thư giãn.
        """)

# Mã HTML5, CSS và JavaScript mô phỏng cảnh đạp xe bình yên
game_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            margin: 0;
            background-color: #1a1a2e;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: sans-serif;
            overflow: hidden;
        }
        #gameCanvas {
            border: 3px solid #e94560;
            border-radius: 12px;
            box-shadow: 0 0 25px rgba(233, 69, 96, 0.4);
            background: linear-gradient(to bottom, #ff7e5f, #feb47b, #ffecd2);
        }
    </style>
</head>
<body>

<canvas id="gameCanvas" width="800" height="450"></canvas>

<script>
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// Trạng thái bàn phím
const keys = {};
window.addEventListener('keydown', e => {
    if(["Space", "ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"].includes(e.code)) {
        e.preventDefault();
    }
    keys[e.code] = true;
});
window.addEventListener('keyup', e => {
    keys[e.code] = false;
});

// Đối tượng người đi xe đạp
const cyclist = {
    x: 200,
    baseY: 340,
    speed: 2,
    distance: 0,
    pedalAngle: 0
};

// Mây trôi
let clouds = [
    {x: 100, y: 60, speed: 0.5, size: 40},
    {x: 400, y: 90, speed: 0.3, size: 60},
    {x: 700, y: 50, speed: 0.4, size: 50}
];

// Cây cối bên đường
let trees = [
    {x: 150, type: 'pine'},
    {x: 350, type: 'round'},
    {x: 550, type: 'pine'},
    {x: 750, type: 'round'},
    {x: 950, type: 'pine'}
];

function update() {
    // Xử lý tốc độ theo phím bấm
    if (keys['KeyD'] || keys['ArrowRight']) {
        cyclist.speed = Math.min(cyclist.speed + 0.05, 4.5);
    } else if (keys['KeyA'] || keys['ArrowLeft']) {
        cyclist.speed = Math.max(cyclist.speed - 0.05, 0.8);
    } else {
        // Tự động duy trì tốc độ dịu dàng nếu không bấm
        if (cyclist.speed > 2) cyclist.speed -= 0.02;
        if (cyclist.speed < 2) cyclist.speed += 0.02;
    }

    cyclist.distance += cyclist.speed;
    cyclist.pedalAngle += cyclist.speed * 0.08;

    // Cập nhật mây
    clouds.forEach(c => {
        c.x -= c.speed;
        if (c.x < -100) c.x = canvas.width + 100;
    });

    // Cập nhật cây cối tạo hiệu ứng parallax (chạy ngang)
    trees.forEach(t => {
        t.x -= cyclist.speed;
        if (t.x < -50) {
            t.x = canvas.width + Math.random() * 100;
            t.type = Math.random() > 0.5 ? 'pine' : 'round';
        }
    });
}

function drawBackground() {
    // Mặt trời hoàng hôn ấm áp
    ctx.fillStyle = '#fffae6';
    ctx.beginPath();
    ctx.arc(680, 130, 45, 0, Math.PI * 2);
    ctx.fill();

    // Dãy núi xa (màu tím mờ ảo)
    ctx.fillStyle = '#6c5b7b';
    ctx.beginPath();
    ctx.moveTo(0, 350);
    ctx.lineTo(0, 250);
    ctx.lineTo(250, 190);
    ctx.lineTo(500, 260);
    ctx.lineTo(800, 180);
    ctx.lineTo(800, 350);
    ctx.closePath();
    ctx.fill();

    // Dãy đồi gần hơn
    ctx.fillStyle = '#355c7d';
    ctx.beginPath();
    ctx.moveTo(0, 350);
    ctx.lineTo(0, 280);
    ctx.quadraticCurveTo(200, 230, 400, 290);
    ctx.quadraticCurveTo(600, 340, 800, 270);
    ctx.lineTo(800, 350);
    ctx.closePath();
    ctx.fill();

    // Mây
    ctx.fillStyle = 'rgba(255, 255, 255, 0.6)';
    clouds.forEach(c => {
        ctx.beginPath();
        ctx.arc(c.x, c.y, c.size * 0.5, 0, Math.PI * 2);
        ctx.arc(c.x + c.size * 0.4, c.y - c.size * 0.2, c.size * 0.4, 0, Math.PI * 2);
        ctx.arc(c.x + c.size * 0.8, c.y, c.size * 0.4, 0, Math.PI * 2);
        ctx.fill();
    });
}

function drawTrees() {
    trees.forEach(t => {
        // Thân cây
        ctx.fillStyle = '#4a3b32';
        ctx.fillRect(t.x - 6, 290, 12, 60);

        // Tán cây
        if (t.type === 'pine') {
            ctx.fillStyle = '#2d4a3e';
            ctx.beginPath();
            ctx.moveTo(t.x, 230);
            ctx.lineTo(t.x - 25, 300);
            ctx.lineTo(t.x + 25, 300);
            ctx.closePath();
            ctx.fill();
        } else {
            ctx.fillStyle = '#3b5e4b';
            ctx.beginPath();
            ctx.arc(t.x, 270, 22, 0, Math.PI * 2);
            ctx.fill();
        }
    });
}

function drawRoad() {
    // Mặt đường
    ctx.fillStyle = '#2c2c54';
    ctx.fillRect(0, 350, canvas.width, 100);

    // Đường kẻ vạch phân cách đứt nét chạy ngang
    ctx.strokeStyle = '#f8b195';
    ctx.lineWidth = 4;
    ctx.setLineDash([20, 20]);
    ctx.lineDashOffset = -cyclist.distance * 2;
    ctx.beginPath();
    ctx.moveTo(0, 395);
    ctx.lineTo(canvas.width, 395);
    ctx.stroke();
    ctx.setLineDash([]); // Reset dash
}

function drawCyclist() {
    const cx = cyclist.x;
    const cy = cyclist.baseY;

    // Hiệu ứng nhún nhẹ khi đạp xe
    const bounce = Math.sin(cyclist.distance * 0.1) * 2;
    const currentY = cy + bounce;

    // Bánh xe sau
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.arc(cx - 25, currentY, 18, 0, Math.PI * 2);
    ctx.stroke();

    // Bánh xe trước
    ctx.beginPath();
    ctx.arc(cx + 25, currentY, 18, 0, Math.PI * 2);
    ctx.stroke();

    // Khung xe đạp
    ctx.strokeStyle = '#e94560';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(cx - 25, currentY); // Trục sau
    ctx.lineTo(cx, currentY - 25);     // Trục giữa (bàn đạp)
    ctx.lineTo(cx + 25, currentY); // Trục trước
    ctx.lineTo(cx + 15, currentY - 35); // Yên xe
    ctx.lineTo(cx, currentY - 25);
    ctx.lineTo(cx + 20, currentY - 42); // Tay lái
    ctx.stroke();

    // Bàn đạp xoay tròn
    const pedalX = cx + Math.cos(cyclist.pedalAngle) * 10;
    const pedalY = (currentY - 25) + Math.sin(cyclist.pedalAngle) * 10;
    ctx.fillStyle = '#ffffff';
    ctx.beginPath();
    ctx.arc(pedalX, pedalY, 4, 0, Math.PI * 2);
    ctx.fill();

    // Người (thân, đầu, tay)
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 4;
    // Thân người ngả về trước
    ctx.beginPath();
    ctx.moveTo(cx, currentY - 25);
    ctx.lineTo(cx + 10, currentY - 55);
    ctx.stroke();

    // Đầu
    ctx.fillStyle = '#ffffff';
    ctx.beginPath();
    ctx.arc(cx + 12, currentY - 63, 7, 0, Math.PI * 2);
    ctx.fill();
}

function drawUI() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.4)';
    ctx.fillRect(15, 15, 180, 50);

    ctx.fillStyle = '#ffffff';
    ctx.font = '14px sans-serif';
    ctx.fillText(`Quãng đường: ${Math.floor(cyclist.distance / 10)} m`, 25, 35);
    ctx.fillText(`Tốc độ gió: ${(cyclist.speed).toFixed(1)} km/h`, 25, 55);
}

function gameLoop() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    update();
    drawBackground();
    drawTrees();
    drawRoad();
    drawCyclist();
    drawUI();

    requestAnimationFrame(gameLoop);
}

gameLoop();
</script>
</body>
</html>
"""

# Nhúng vào Streamlit
components.html(game_html, height=480)
