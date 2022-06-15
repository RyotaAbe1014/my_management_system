<template>
  <v-app>
    <v-card width="400px" class="mx-auto mt-5 login-card">
      <v-card-title>
        <h1 class="display-1 mx-auto">ログイン</h1>
      </v-card-title>
      <v-card-text>
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-text-field
            prepend-icon="mdi-account-circle"
            v-model="email"
            :rules="emailRules"
            label="メールアドレス"
            required
          />
          <v-text-field
            prepend-icon="mdi-lock"
            v-model="password"
            type="password"
            label="パスワード"
            required
          />
            <v-alert
              dense
              outlined
              type="error"
              class="error-msg"
              v-if="errorMessage"
              >{{ errorMessage }}
            </v-alert>
          <v-card-actions>
            <v-btn
              class="deep-purple accent-4 mx-auto"
              :disabled="isValid"
              @click="submit"
              dark
              >ログイン</v-btn
            >
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
      valid: true,
      email: "",
      emailRules: [
        (v) => !!v || "メールアドレスを入力してください",
        (v) => /.+@.+\..+/.test(v) || "メールアドレスが不正です",
      ],
      password: "",
      accessToken: null,
      errorMessage: null,
    };
  },
  computed: {
    isValid() {
      console.log("isValid", this.valid);
      return !this.valid;
    },
  },
  methods: {
    validate() {
      this.$refs.form.validate();
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
    async submit() {
      console.log("submit call");
      await this.axios
        .post("http://0.0.0.0:8000/api/auth/jwt/create/", {
          email: this.email,
          password: this.password,
        })
        .then((response) => {
          console.log(response.data.access);
          this.accessToken = response.data.access;
          this.axios
            .get("http://0.0.0.0:8000/api/auth/users/me/", {
              headers: { Authorization: "JWT " + this.accessToken },
            })
            .then((response) => {
              console.log(response);
              const auth = {
                id: response.data.id,
                name: response.data.name,
                email: response.data.email,
                accessToken: this.accessToken,
              };
              sessionStorage.setItem("user", JSON.stringify(auth));
              this.$router.push("/");
            })
            .catch((e) => {
              console.log("エラー", e);
            });
        })
        .catch((e) => {
          console.log("エラー", e);
          this.errorMessage = "ログインに失敗しました";
        });
    },
  },
};
</script>
<style lang="scss" scoped>
.login-card {
  top: 200px;
}
</style>