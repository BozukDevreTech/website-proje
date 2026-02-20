const videolar = [
    {
        baslik: "Html_Ders_1",
        aciklama: "web sitesi tasarlamak için güzel bir başlangıç...",
        resim: "https://img.youtube.com/vi/UmptMlrkwJE/hqdefault.jpg",
        link: "https://www.youtube.com/watch?v=UmptMlrkwJE"
    },
    {
        baslik: "C++_Ders_1",
        aciklama: "Yazılım öğrenmenin mantığını ve temellerini atabileceğiniz yerinde bir başlangıç.",
        resim: "https://img.youtube.com/vi/I6nzfDjiY9o/hqdefault.jpg",
        link: "https://www.youtube.com/watch?v=I6nzfDjiY9o"
    },
    {
        baslik: "Kontrol_Kulesi_Arduino_Projem",
        aciklama: "Sadece yazılımla yetinmeyip, aynı zamanda arduino projelerimi hayata geçiriyorum",
        resim: "https://img.youtube.com/vi/o0KclqH9ArM/hqdefault.jpg",
        link: "https://www.youtube.com/watch?v=o0KclqH9ArM"
        
    }
];

// 1. kart
document.querySelector(".kart-resim").src = videolar[0].resim;
document.querySelector(".kart-baslik").textContent = videolar[0].baslik;
document.querySelector(".kart-aciklama").textContent = videolar[0].aciklama;

document.querySelector(".onerilen-kart").onclick = function() {
    window.open(videolar[0].link, "_blank");
};


// 2. kart
document.querySelector(".kart-resim-2").src = videolar[1].resim;
document.querySelector(".kart-baslik-2").textContent = videolar[1].baslik;
document.querySelector(".kart-aciklama-2").textContent = videolar[1].aciklama;

document.querySelectorAll(".onerilen-kart")[1].onclick = function() {
    window.open(videolar[1].link, "_blank");
};


// 3. kart
document.querySelector(".kart-resim-3").src = videolar[2].resim;
document.querySelector(".kart-baslik-3").textContent = videolar[2].baslik;
document.querySelector(".kart-aciklama-3").textContent = videolar[2].aciklama;

document.querySelectorAll(".onerilen-kart")[2].onclick = function() {
    window.open(videolar[2].link, "_blank");
};