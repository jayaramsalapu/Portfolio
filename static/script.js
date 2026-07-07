document.addEventListener("DOMContentLoaded", () => {
    /* ==========================================================================
       SELECTORS & CONSTANTS
       ========================================================================== */
    const navbar = document.querySelector(".navbar-header");
    const mobileMenuBtn = document.querySelector(".mobile-hamburger");
    const navMenu = document.querySelector(".navbar-menu-wrapper");
    const navLinks = document.querySelectorAll(".navbar-nav-link");
    const sections = document.querySelectorAll("section[id]");
    const scrollProgressBar = document.querySelector(".scroll-progress-bar");
    const backToTopBtn = document.querySelector(".back-to-top-btn");
    const typingTextEl = document.getElementById("typing-text");

    /* ==========================================================================
       MOBILE MENU TOGGLE
       ========================================================================== */
    if (mobileMenuBtn && navMenu) {
        mobileMenuBtn.addEventListener("click", () => {
            mobileMenuBtn.classList.toggle("active");
            navMenu.classList.toggle("active");
            document.body.classList.toggle("overflow-hidden");
        });

        // Close mobile menu on link click
        navLinks.forEach(link => {
            link.addEventListener("click", () => {
                mobileMenuBtn.classList.remove("active");
                navMenu.classList.remove("active");
                document.body.classList.remove("overflow-hidden");
            });
        });
    }

    /* ==========================================================================
       STICKY NAVBAR & SCROLL PROGRESS & BACK TO TOP
       ========================================================================== */
    const handleScroll = () => {
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        
        // Sticky Navbar
        if (navbar) {
            if (scrollTop > 20) {
                navbar.classList.add("scrolled");
            } else {
                navbar.classList.remove("scrolled");
            }
        }

        // Scroll Progress Bar
        if (scrollProgressBar && scrollHeight > 0) {
            const scrollPercentage = (scrollTop / scrollHeight) * 100;
            scrollProgressBar.style.width = `${scrollPercentage}%`;
        }

        // Back To Top Button
        if (backToTopBtn) {
            if (scrollTop > 400) {
                backToTopBtn.classList.add("visible");
            } else {
                backToTopBtn.classList.remove("visible");
            }
        }

        // Active Nav Link Highlighting
        let currentSectionId = "";
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 120;
            const sectionHeight = section.offsetHeight;
            if (scrollTop >= sectionTop && scrollTop < sectionTop + sectionHeight) {
                currentSectionId = section.getAttribute("id");
            }
        });

        navLinks.forEach(link => {
            link.classList.remove("active");
            if (link.getAttribute("href") === `#${currentSectionId}`) {
                link.classList.add("active");
            }
        });
    };

    window.addEventListener("scroll", handleScroll);
    handleScroll(); // Trigger on page load

    // Back to Top action
    if (backToTopBtn) {
        backToTopBtn.addEventListener("click", () => {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        });
    }

    /* ==========================================================================
       VANILLA TYPEWRITER ANIMATION
       ========================================================================== */
    if (typingTextEl) {
        const primaryText = typingTextEl.getAttribute("data-profession") || typingTextEl.innerText;
        const alternativeTexts = [
            primaryText,
        ].filter((val, index, self) => val && self.indexOf(val) === index); // Unique values only

        let phraseIndex = 0;
        let charIndex = 0;
        let deleting = false;

        const typeLoop = () => {
            const currentPhrase = alternativeTexts[phraseIndex];
            
            if (deleting) {
                typingTextEl.innerText = currentPhrase.substring(0, charIndex - 1);
                charIndex--;
            } else {
                typingTextEl.innerText = currentPhrase.substring(0, charIndex + 1);
                charIndex++;
            }

            let typeSpeed = deleting ? 35 : 85;

            if (!deleting && charIndex === currentPhrase.length) {
                typeSpeed = 1800; // Pause at full word
                deleting = true;
            } else if (deleting && charIndex === 0) {
                deleting = false;
                phraseIndex = (phraseIndex + 1) % alternativeTexts.length;
                typeSpeed = 400; // Pause before typing next word
            }

            setTimeout(typeLoop, typeSpeed);
        };

        typingTextEl.innerText = "";
        setTimeout(typeLoop, 800);
    }



    /* ==========================================================================
       BUTTON RIPPLE EFFECT
       ========================================================================== */
    const buttons = document.querySelectorAll(".btn");
    buttons.forEach(btn => {
        btn.addEventListener("click", function(e) {
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const ripple = document.createElement("span");
            ripple.style.position = "absolute";
            ripple.style.left = `${x}px`;
            ripple.style.top = `${y}px`;
            ripple.style.width = "20px";
            ripple.style.height = "20px";
            ripple.style.backgroundColor = "rgba(255, 255, 255, 0.4)";
            ripple.style.borderRadius = "50%";
            ripple.style.transform = "translate(-50%, -50%) scale(0)";
            ripple.style.animation = "ripple-animation 0.6s ease-out";
            ripple.style.pointerEvents = "none";

            // Add animation keyframes inline if not present
            if (!document.getElementById("ripple-style-rules")) {
                const style = document.createElement("style");
                style.id = "ripple-style-rules";
                style.innerHTML = `
                    @keyframes ripple-animation {
                        to {
                            transform: translate(-50%, -50%) scale(25);
                            opacity: 0;
                        }
                    }
                `;
                document.head.appendChild(style);
            }

            this.appendChild(ripple);
            setTimeout(() => ripple.remove(), 600);
        });
    });
});
