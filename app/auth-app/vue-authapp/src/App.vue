<template>
    <div id="app" class="app-wrapper">
        <header class="bg-dark">
            <b-navbar class="w-75 mx-auto" type="dark" variant="dark">
                <b-navbar-brand>ФГУП «ГРЧЦ»</b-navbar-brand>
                <b-navbar-nav>
                    <b-nav-item href="#">Тестовое задание</b-nav-item>
                </b-navbar-nav>
            </b-navbar>
        </header>

        <main class="container-fluid my-5">
            <router-view />
        </main>

        <footer>
            <b-jumbotron bg-variant="dark" text-variant="white" class="rounded-0 mb-0">
                <div class="w-75 mx-auto">
                    <div class="row">
                        <div class="col-4 text-left mt-5">© ФГУП «ГРЧЦ», 2022</div>
                        <div class="col-4 text-center mt-5">Тестовое задание</div>
                    </div>
                </div>
            </b-jumbotron>
        </footer>
    </div>
</template>

<script>
export default {
    name: 'App',
};
</script>

<style>
    .navbar,
    .navbar-brand {
        font-size: 16pt;
    }

    header {
        height: 70px;
    }

    main {
        height: calc(100vh - 160px - 70px * 2);
        min-height: 600px;
    }

    footer {
        margin-top: 120px;
        font-size: 20pt;
    }

    footer .jumbotron {
        height: 160px;
    }
</style>
