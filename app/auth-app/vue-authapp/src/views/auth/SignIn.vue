<template>
    <base-auth-layout>
        <sign-in-form />
    </base-auth-layout>
</template>

<script>
import SignInForm from '@/components/auth/SignInForm';
import BaseAuthLayout from '@/layouts/BaseAuthLayout';

export default {
    name: 'SignIn',
    components: { SignInForm, BaseAuthLayout },
};
</script>
