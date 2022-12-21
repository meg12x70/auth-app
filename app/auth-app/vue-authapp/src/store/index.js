import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import { AccessLevel } from '../services/consts';

Vue.use(Vuex);

export default new Vuex.Store({
    actions: {
        fetchAuthUser(ctx) {
            axios
                .get('http://127.0.0.1:8000/api/auth/users/me/', {
                    headers: {
                        Authorization: `Token ${localStorage.getItem('token')}`,
                    },
                })
                // eslint-disable-next-line
                .then(response => axios
                    .get(`http://127.0.0.1:8000/api/appusers/${response.data.id}`)
                    .then((res) => {
                        let districts;
                        if (res.data.access_level === AccessLevel.LOW) {
                            districts = ['ДФО'];
                        } else if (res.data.access_level === AccessLevel.MIDDLE) {
                            districts = ['СФО', 'СЗФО'];
                        } else {
                            districts = ['ДФО', 'ЦФО', 'УФО', 'СФО', 'СЗФО'];
                        }
                        ctx.commit('updateAccessLevel', { id: res.data.access_level, access_districts: districts });
                    }),
                );
        },
    },
    mutations: {
        updateAccessLevel(state, level) {
            state.accessLevel = level;
        },
    },
    state: {
        accessLevel: {},
    },
    getters: {
        accessLevel(state) {
            return state.accessLevel;
        },
    },
});
