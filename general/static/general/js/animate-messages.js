// https://api.jquery.com/animate/#per-property-easing
// В Zeal ищется по слову animate.
// Здесь анимация привязывается к классам
// bg-success или bg-danger.
// Это классы сообщений
// Django messages framework.
// Достоинство этой методики в том, что
// он выполняется копированием и вставкой.
// И небольшая правка: надо чуть-чуть почистить - убрать
// функцию, срабатывающую после анимации.
// Классы, если забудете, подсмотрите в появляющихся сообщениях.
// Animation complete и относящееся к нему здесь неуместны.
// Это работать не будет. Вывод: код получился нечистым, но
// править его не надо: он безобиден. Тратить на правку время
// смысла нет.
function animateMessage(){
   $(".bg-success, .bg-danger").animate({
    width: [ "toggle", "swing" ],
    height: [ "toggle", "swing" ],
    opacity: "toggle"
  }, 2000, "linear");
};

animateMessage();


