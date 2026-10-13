/* Gold visual effects: floating gold dust + count-up numbers */
(function () {
    var reduce = window.matchMedia &&
        window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    /* ---------- COUNT-UP NUMBERS (dashboard stat cards) ---------- */
    function countUp() {
        if (reduce) return;
        document.querySelectorAll(".stat-card-value").forEach(function (el) {
            var text = el.textContent.trim();
            var m = text.match(/^(\D*)([\d,]+(?:\.\d+)?)(.*)$/);
            if (!m) return;

            var prefix = m[1];
            var raw = m[2].replace(/,/g, "");
            var target = parseFloat(raw);
            var suffix = m[3];
            var decimals = raw.indexOf(".") > -1 ? raw.split(".")[1].length : 0;
            if (!isFinite(target) || target === 0) return;

            var start = null;
            var duration = 1100;

            function format(v) {
                return prefix + v.toLocaleString("en-IN", {
                    minimumFractionDigits: decimals,
                    maximumFractionDigits: decimals
                }) + suffix;
            }

            function step(ts) {
                if (start === null) start = ts;
                var p = Math.min((ts - start) / duration, 1);
                var eased = 1 - Math.pow(1 - p, 3);
                el.textContent = format(target * eased);
                if (p < 1) requestAnimationFrame(step);
                else el.textContent = format(target);
            }

            el.textContent = format(0);
            requestAnimationFrame(step);
        });
    }

    /* ---------- GOLD DUST ---------- */
    function goldDust() {
        if (reduce) return;

        var canvas = document.getElementById("goldDust");
        if (!canvas) {
            canvas = document.createElement("canvas");
            canvas.id = "goldDust";
            document.body.appendChild(canvas);
        }

        var ctx = canvas.getContext("2d");
        var w = 0, h = 0, dpr = Math.min(window.devicePixelRatio || 1, 2);
        var particles = [];

        function resize() {
            w = window.innerWidth;
            h = window.innerHeight;
            canvas.width = w * dpr;
            canvas.height = h * dpr;
            ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
            var count = Math.max(24, Math.min(70, Math.round(w / 22)));
            while (particles.length < count) particles.push(make(true));
            particles.length = count;
        }

        function make(anywhere) {
            return {
                x: Math.random() * w,
                y: anywhere ? Math.random() * h : h + 10,
                r: 0.5 + Math.random() * 1.6,
                vy: 0.12 + Math.random() * 0.4,
                vx: (Math.random() - 0.5) * 0.15,
                a: Math.random() * Math.PI * 2,
                s: 0.01 + Math.random() * 0.025
            };
        }

        var running = true;
        document.addEventListener("visibilitychange", function () {
            running = !document.hidden;
            if (running) requestAnimationFrame(draw);
        });

        function draw() {
            if (!running) return;
            ctx.clearRect(0, 0, w, h);
            for (var i = 0; i < particles.length; i++) {
                var p = particles[i];
                p.y -= p.vy;
                p.x += p.vx + Math.sin(p.a) * 0.1;
                p.a += p.s;
                if (p.y < -10) particles[i] = make(false);

                var alpha = 0.25 + 0.55 * Math.abs(Math.sin(p.a * 1.4));
                ctx.beginPath();
                ctx.fillStyle = "rgba(255, 214, 110," + alpha.toFixed(2) + ")";
                ctx.shadowColor = "rgba(245, 196, 81, 0.9)";
                ctx.shadowBlur = 8;
                ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                ctx.fill();
            }
            requestAnimationFrame(draw);
        }

        window.addEventListener("resize", resize);
        resize();
        requestAnimationFrame(draw);
    }

    document.addEventListener("DOMContentLoaded", function () {
        goldDust();
        countUp();
    });
})();