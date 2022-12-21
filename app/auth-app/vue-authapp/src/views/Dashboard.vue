<template>
    <div class="dashboard">
        <div class="dashboard__navbar">
            <div
                class="dashboard__navbar-item"
                @click="currentTabIndex = index + 1"
                v-for="(tab, index) in tabs"
                :key="index"
                v-if="tab.access.includes(accessLevel.id)"
            >
                {{ tab.name }}
            </div>
        </div>

        <div class="dashboard__tables">
            <div
                class="dashboard__table"
                v-for="(tab, index) in tabs"
                :key="index"
                v-if="tab.access.includes(accessLevel.id) && currentTabIndex === index + 1"
            >
                <div
                    v-for="(item, index) in tab.tableItems"
                    :key="index"
                    v-if="getCurrentDistricts(item)"
                >
                    {{ item }}
                </div>
                <div v-else>
                    Нет доступных данных
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { AccessLevel } from '../services/consts';

export default {
    name: 'Dashboard',
    data() {
        return {
            tabs: [
                {
                    name: 'Пункт Меню 1',
                    tableItems: ['ДФО', 'ЦФО', 'ДФО', 'УФО', 'ЦФО'],
                    access: [AccessLevel.LOW, AccessLevel.HIGH],
                },
                {
                    name: 'Пункт Меню 2',
                    tableItems: ['ЦФО', 'ДФО', 'ЦФО', 'СФО', 'СЗФО', 'ДФО'],
                    access: [AccessLevel.LOW, AccessLevel.MIDDLE, AccessLevel.HIGH],
                },
                {
                    name: 'Пункт Меню 3',
                    tableItems: ['СФО', 'ЦФО', 'СФО', 'УФО', 'СЗФО'],
                    access: [AccessLevel.MIDDLE, AccessLevel.HIGH],
                },
            ],
            currentTabIndex: 2,
        };
    },
    computed: {
        ...mapGetters([
            'accessLevel',
        ]),
    },
    methods: {
        getCurrentDistricts(item) {
            return this.accessLevel.access_districts.includes(item);
        },
    },
};
</script>

<style>
    :root {
        --primary: #485CC7;
        --white: #ffffff;
    }
    .dashboard {
        display: grid;
        grid-template-columns: 250px 1fr;
        grid-template-areas: "nav tables";
        height: 100%;
    }

    .dashboard__navbar {
        grid-area: nav;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 25px;
        padding: 25px;
        border-right: 0.5px solid var(--primary);
    }

    .dashboard__tables {
        grid-area: tables;
        display: flex;
        justify-content: center;
        padding: 32px;
    }

    .dashboard__navbar-item {
        transition: 0.2s;
        cursor: pointer;
    }

    .dashboard__navbar-item:hover {
        color: var(--primary);
    }

    .dashboard__table {
        display: flex;
        flex-direction: column;
        align-items: center;
        height: max-content;
        width: 60%;
        gap: 20px;
        padding: 32px;
        border: 1px solid var(--primary);
        border-radius: 16px;
        transition: 0.2s;
    }

    .dashboard__table:hover {
        color: var(--white);
        background-color: var(--primary);
    }

    .dashboard__table:hover {
        background-color: var(--primary);
    }
</style>
