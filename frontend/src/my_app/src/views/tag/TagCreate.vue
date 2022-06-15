<template>
  <v-app id="inspire">
    <AppBar />
    <v-main class="grey lighten-2">
      <v-container>
        <h1>タグ作成</h1>
        <v-container>
          <v-row>
            <v-col cols="4" class="white d-flex flex-wrap">
              <v-alert
                dense
                outlined
                type="error"
                class="error-msg"
                v-if="errorMessage"
                >{{ errorMessage }}
              </v-alert>
              <v-form
                ref="form"
                v-model="valid"
                lazy-validation
                class="ml-10 d-flex align-center"
              >
                <v-text-field
                  v-model="tagName"
                  :rules="tagNameRules"
                  label="タグ名"
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
  name: "TagCreate",
  components: {
    AppBar,
  },
  data() {
    return {
      tagName: "",
      valid: true,
      tagNameRules: [(v) => !!v || "タグ名を入力してください"],
      auth: [],
      accessToken: null,
      errorMessage: null,
    };
  },
  mounted() {
    this.auth = JSON.parse(sessionStorage.getItem("user"));
    this.accessToken = this.auth.accessToken;
    console.log(this.accessToken);
  },
  methods: {
    async validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        console.log(this.tagName);
        await this.axios
          .post(
            "http://0.0.0.0:8000/api/tag/index/",
            {
              name: this.tagName,
            },
            { headers: { Authorization: "JWT " + this.accessToken } }
          )
          .then((response) => {
            console.log(response);
            this.$router.push("/tag");
          })
          .catch((e) => {
            console.log("タグ作成に失敗しました", e);
            this.errorMessage = "タグ作成に失敗しました";
          });
      }
    },
  },
  computed: {},
};
</script>