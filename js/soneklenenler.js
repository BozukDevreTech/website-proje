const gonderiler = [

    {
        tarih: "Sponsorluk:",
        baslik: "https://short-url.org/1piNy",
    },

    {
        tarih: "Tam Bizlik Serisi Projeler:",
        baslik: "https://short-url.org/1piNL",
    },

    {
        tarih: "12 Ağustos 2025:",
        baslik: "https://short-url.org/1piNP",
    }

];


// HTML'deki boş yerleri bulur
const tarihler = document.querySelectorAll(".tarih");
const basliklar = document.querySelectorAll(".baslik");


// htmldeki kısımların içlerini doldurur
for (let i = 0; i < gonderiler.length; i++) {

    tarihler[i].textContent = gonderiler[i].tarih;

    basliklar[i].textContent = gonderiler[i].baslik;

    basliklar[i].href = gonderiler[i].baslik;   //bağlantıya tıklanınca açılacak

    basliklar[i].target = "_blank";             //yeni sekmede açılacak
}