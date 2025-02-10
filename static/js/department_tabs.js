document.addEventListener("DOMContentLoaded", function () {
    const tabs = document.querySelectorAll(".tab-btn");
    const contents = document.querySelectorAll(".tab-content");

    tabs.forEach(tab => {
        tab.addEventListener("click", function () {
            const target = this.id.replace("tab-", "");

            // Barcha contentlarni yashirish
            contents.forEach(content => content.classList.add("hidden"));

            // Barcha tab tugmalaridan active classlarini olib tashlash
            tabs.forEach(t => {
                t.classList.remove("text-blue-600", "border-blue-600");
                t.classList.add("text-gray-500", "border-transparent");
            });

            // Tanlangan contentni ko‘rsatish
            document.getElementById(target)?.classList.remove("hidden");

            // Tanlangan tugmani aktiv qilish
            this.classList.add("text-blue-600", "border-blue-600");
            this.classList.remove("text-gray-500", "border-transparent");
        });
    });
});
