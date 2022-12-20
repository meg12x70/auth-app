<template>
    <base-auth-layout>
        <sign-up-form />
    </base-auth-layout>
</template>

<script>
import SignUpForm from '@/components/auth/SignUpForm';
import BaseAuthLayout from '@/layouts/BaseAuthLayout';

export default {
    name: 'SignUp',
    components: { SignUpForm, BaseAuthLayout },
};
</script>
