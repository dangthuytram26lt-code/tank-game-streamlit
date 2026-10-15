import streamlit as st
import streamlit.components.v1 as components

# Cấu hình giao diện trang Streamlit
st.set_page_config(
    page_title="Chiến Tranh Xe Tăng",
    page_icon="⚔️",
    layout="wide"
)

st.title("⚔️ Game Chiến Tranh Xe Tăng")
st.caption("Game bắn xe tăng mượt mà tích hợp HTML5 & Python trên Streamlit")

# Giao diện hướng dẫn
with st.expander("📖 Hướng dẫn điều khiển", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        * **Di chuyển:** Nhấn phím `W` (Lên), `S` (Xuống), `A` (Trái), `D` (Phải)
        * **Bắn đạn:** Nhấn phím `Space` (Khoảng trắng)
        """)
    with col2:
        st.markdown("""
        * **Mục tiêu:** Tiêu diệt xe tăng màu đỏ để tích điểm.
        * **Lưu ý:** Xe tăng địch sẽ tự di chuyển và bắn lại bạn!
        """)

# Mã HTML5 / JavaScript xử lý Game real-time
game_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            margin: 0;
            background-color: #1e1e1e;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        canvas {
            border: 3px solid #4CAF50;
            background-color: #0d1117;
            box-shadow: 0 0 15px rgba(76, 175, 80, 0.4);
        }
    </style>
</head>
<body>

<canvas id="gameCanvas" width="800" height="500"></canvas>

<script>
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

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

const player = {
    x: 400,
    y: 400,
    size: 28,
    speed: 4,
    color: '#4CAF50',
    angle: 0,
    score: 0,
    health: 100,
    lastShoot: 0
};

let bullets = [];
let enemyBullets = [];
let enemies = [];
let gameOver = false;

function spawnEnemy() {
    if (enemies.length < 5 && !gameOver) {
        enemies.push({
            x: Math.random() * (canvas.width - 60) + 30,
            y: Math.random() * 150 + 30,
            size: 28,
            speed: 1.5,
            color: '#E53935',
            lastShoot: 0
        });
    }
}
setInterval(spawnEnemy, 2000);

function updatePlayer() {
    let dx = 0;
    let dy = 0;

    if (keys['KeyA'] || keys['ArrowLeft']) dx -= 1;
    if (keys['KeyD'] || keys['ArrowRight']) dx += 1;
    if (keys['KeyW'] || keys['ArrowUp']) dy -= 1;
    if (keys['KeyS'] || keys['ArrowDown']) dy += 1;

    if (dx !== 0 || dy !== 0) {
        player.angle = Math.atan2(dy, dx);
        player.x += dx * player.speed;
        player.y += dy * player.speed;

        player.x = Math.max(player.size, Math.min(canvas.width - player.size, player.x));
        player.y = Math.max(player.size, Math.min(canvas.height - player.size, player.y));
    }

    const now = Date.now();
    if (keys['Space'] && now - player.lastShoot > 200) {
        bullets.push({
            x: player.x,
            y: player.y,
            vx: Math.cos(player.angle) * 7,
            vy: Math.sin(player.angle) * 7
        });
        player.lastShoot = now;
    }
}

function updateEnemies() {
    const now = Date.now();
    enemies.forEach((enemy) => {
        const angle = Math.atan2(player.y - enemy.y, player.x - enemy.x);
        enemy.x += Math.cos(angle) * enemy.speed;
        enemy.y += Math.sin(angle) * enemy.speed;

        if (now - enemy.lastShoot > 1500) {
            enemyBullets.push({
                x: enemy.x,
                y: enemy.y,
                vx: Math.cos(angle) * 5,
                vy: Math.sin(angle) * 5
            });
            enemy.lastShoot = now;
        }
    });
}

function updateBullets() {
    bullets.forEach((b, bIdx) => {
        b.x += b.vx;
        b.y += b.vy;

        enemies.forEach((e, eIdx) => {
            const dist = Math.hypot(b.x - e.x, b.y - e.y);
            if (dist < e.size / 2 + 5) {
                enemies.splice(eIdx, 1);
                bullets.splice(bIdx, 1);
                player.score += 10;
            }
        });
    });

    enemyBullets.forEach((eb, ebIdx) => {
        eb.x += eb.vx;
        eb.y += eb.vy;

        const dist = Math.hypot(eb.x - player.x, eb.y - player.y);
        if (dist < player.size / 2 + 5) {
            enemyBullets.splice(ebIdx, 1);
            player.health -= 20;
            if (player.health <= 0) {
                gameOver = true;
            }
        }
    });

    bullets = bullets.filter(b => b.x > 0 && b.x < canvas.width && b.y > 0 && b.y < canvas.height);
    enemyBullets = enemyBullets.filter(eb => eb.x > 0 && eb.x < canvas.width && eb.y > 0 && eb.y < canvas.height);
}

function drawTank(x, y, size, color, angle = 0) {
    ctx.save();
    ctx.translate(x, y);
    ctx.rotate(angle);

    ctx.fillStyle = color;
    ctx.fillRect(-size/2, -size/2, size, size);

    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, -3, size/1.2, 6);

    ctx.restore();
}

function gameLoop() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (!gameOver) {
        updatePlayer();
        updateEnemies();
        updateBullets();

        drawTank(player.x, player.y, player.size, player.color, player.angle);

        enemies.forEach(e => {
            const angle = Math.atan2(player.y - e.y, player.x - e.x);
            drawTank(e.x, e.y, e.size, e.color, angle);
        });

        ctx.fillStyle = '#FFD700';
        bullets.forEach(b => {
            ctx.beginPath();
            ctx.arc(b.x, b.y, 4, 0, Math.PI * 2);
            ctx.fill();
        });

        ctx.fillStyle = '#FF5722';
        enemyBullets.forEach(eb => {
            ctx.beginPath();
            ctx.arc(eb.x, eb.y, 4, 0, Math.PI * 2);
            ctx.fill();
        });

        ctx.fillStyle = '#ffffff';
        ctx.font = '16px sans-serif';
        ctx.fillText(`Máu: ${player.health}%`, 20, 30);
        ctx.fillText(`Điểm: ${player.score}`, 20, 55);
    } else {
        ctx.fillStyle = '#E53935';
        ctx.font = '36px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('GAME OVER', canvas.width / 2, canvas.height / 2 - 20);

        ctx.fillStyle = '#ffffff';
        ctx.font = '18px sans-serif';
        ctx.fillText(`Tổng điểm: ${player.score}`, canvas.width / 2, canvas.height / 2 + 20);
        ctx.fillText('Tải lại trang (F5) để chơi lại', canvas.width / 2, canvas.height / 2 + 50);
    }

    requestAnimationFrame(gameLoop);
}

gameLoop();
</script>
</body>
</html>
"""

# Hiển thị Game trong ứng dụng Streamlit
components.html(game_code, height=530)
