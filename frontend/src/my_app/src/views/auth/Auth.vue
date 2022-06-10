<template>
  <v-app>
     <v-card width="400px" class="mx-auto mt-5 login-card">
      <v-card-title>
        <h1 class="display-1 mx-auto">ログイン</h1>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field prepend-icon="mdi-account-circle" label="ユーザ名" />
          <v-text-field
            prepend-icon="mdi-lock"
            label="パスワード"
            type="password"
          />
          <v-card-actions >
             <v-btn class="deep-purple accent-4 mx-auto" dark>ログイン</v-btn>
          </v-card-actions>
        </v-form>
      </v-card-text>
    </v-card>
  </v-app>
</template>

<script>
export default {
  name: "Auth",
  data() {
    return {

    };
  },
};
</script>
<style lang="scss" scoped>
.login-card {
  top: 200px;
}
</style>