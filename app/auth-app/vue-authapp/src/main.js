// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import Vuelidate from 'vuelidate';
import { BootstrapVue } from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import router from '@/router/index';
import App from './App';

Vue.use(VueAxios, axios);
Vue.use(BootstrapVue);
Vue.use(router);
Vue.use(Vuelidate);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
    render: h => h(App),
    router,
    axios,
}).$mount('#app');
