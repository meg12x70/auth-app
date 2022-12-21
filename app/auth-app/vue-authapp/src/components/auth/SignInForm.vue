<template>
    <b-form @submit.prevent="login">
        <div class="form-group">
            <label for="username">
                Логин:
            </label>

            <b-input v-model="form.username" type="text" id="username" placeholder="Логин...">
            </b-input>
        </div>

        <div class="form-group mt-4">
            <label for="password">
                Пароль:
            </label>

            <b-input v-model="form.password" type="password" id="password" placeholder="Пароль...">
            </b-input>
        </div>

        <b-button variant="primary" type="submit" class="mt-4">
            Войти
        </b-button>

        <p class="mt-3">
            Ещё не зарегистрированы?

            <router-link to="/auth/signup">
                Регистрация
            </router-link>
        </p>
    </b-form>
</template>
<script>
import { mapActions } from 'vuex';
import authRequest from '@/mixins/authRequest';

export default {
    name: 'SignInForm',
    data() {
        return {
            form: {
                username: '',
                password: '',
            },
        };
    },
    mixins: [authRequest],
    methods: {
        ...mapActions([
            'fetchAuthUser',
        ]),
        async login() {
            // логика авторизации
            try {
                const response = await this.authRequest('auth/token', this.form);

                // авторизуем юзера
                // eslint-disable-next-line
                if (response) {
                    this.setLogined(response.token);
                    this.$router.push('/dashboard');
                }
            } catch (error) {
                /* eslint no-console: ["error", { allow: ["warn", "error"] }] */
                console.error('AN API ERROR:', error);
            }
        },

        setLogined(token) {
            // сохраняем токен
            // eslint-disable-next-line
            localStorage.setItem('token', token);
            this.fetchAuthUser();
        },
    },
};
</script>
