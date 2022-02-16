// NPM modules.
import Vue from 'vue';

// Vue components.
import App from './app.vue';

/*/ FontAwesome modules.
import { library } from '@fortawesome/fontawesome-svg-core';
import {
  faTwitterSquare, faFacebookSquare, faLinkedin, faYoutubeSquare
} from '@fortawesome/free-brands-svg-icons';
import {
  faTrashAlt, faTimes, faRedoAlt, faFileDownload, faFileUpload
} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';*/

// CSS.
import './assets/css/global.css';

/*/ Setup FontAwesome icons.
library.add(faTwitterSquare,
            faFacebookSquare,
            faLinkedin,
            faYoutubeSquare,
            faTrashAlt,
            faTimes,
            faRedoAlt,
            faFileDownload,
            faFileUpload);
Vue.component('font-awesome-icon', FontAwesomeIcon);*/

// Enable v-tooltip.
//Vue.use(VTooltip);

// Instantiate main Vue instance.
new Vue({
    render(h) { return h(App); }
}).$mount('#app');