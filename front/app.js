
// document.addEventListener( 'DOMContentLoaded', function () {
//     new Splide( '#card-carousel', {
//           perPage    : 2,
//           breakpoints: {
//               640: {
//                   perPage: 1,
//               },
//           },
//     } ).mount();
//   } );



//   document.addEventListener( 'DOMContentLoaded', function () {
//     new Splide( '#fullscreen-carousel', {
//           width : '100vw',
//           height: '100vh',
//     } ).mount();
//   } );







new Splide( '.splide', {
    autoWidth: true,
    focus    : 0,
    omitEnd  : true,
  } );



  var splide = new Splide( '.splide', {
  type     : 'loop',
  height   : '10rem',
  focus    : 'center',
  autoWidth: true,
} );

splide.mount();