<template>
  <v-app id="inspire">
    <AppBar />
    <v-main class="grey lighten-2">
      <v-container>
        <h1>目標作成</h1>
        <v-container>
          <v-row>
            <v-col cols="7" class="white d-flex flex-wrap">
              <v-form
                ref="form"
                v-model="valid"
                lazy-validation
                class="ml-10 d-flex align-center"
              >
                <v-text-field
                  v-model="target"
                  :rules="targetRules"
                  label="目標"
                  required
                ></v-text-field>
                <v-btn
                  :disabled="!valid"
                  color="success"
                  @click="validate"
                  class="ml-4"
                >
                  作成
                </v-btn>
              </v-form>
            </v-col>
          </v-row>
        </v-container>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import AppBar from "../../components/layouts/AppBar.vue";
export default {
  name: "CreateTarget",
  components: {
    AppBar,
  },
  data() {
    return {
      valid: true,
      targetRules: [(v) => !!v || "内容を入力してください"],
      auth: [],
      accessToken: null,
      userId: null,
      target: null,
    };
  },
  mounted() {
    this.auth = JSON.parse(sessionStorage.getItem("user"));
    this.accessToken = this.auth.accessToken;
    this.userId = this.auth.id;
  },
  methods: {
    async validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        await this.axios
          .post(
            "http://0.0.0.0:8000/api/target_management/index/",
            {
              user: this.userId,
              name: this.target,
            },
            { headers: { Authorization: "JWT " + this.accessToken } }
          )
          .then((response) => {
            console.log(response);
            this.target = "";
          })
          .catch((e) => {
            console.log("目標作成に失敗しました", e);
            console.log(e.request);
          });
      }
    },
  },
  computed: {},
};
</script>
<style scoped>
.v-text-field {
  width: 400px;
}
</style>