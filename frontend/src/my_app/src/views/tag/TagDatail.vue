<template>
  <v-app id="inspire">
    <AppBar />
    <v-main class="grey lighten-2">
      <v-container>
        <h1>タグ編集</h1>
        <v-container>
          <v-row>
            <v-col cols="4" class="white d-flex flex-wrap">
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
                  編集
                </v-btn>
                <v-btn color="error" @click="deleteTag" class="ml-4">
                  削除
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
  name: "TagDatail",
  components: {
    AppBar,
  },
  data() {
    return {
      tag: null,
      tagId: null,
      tagName: "",
      valid: true,
      tagNameRules: [(v) => !!v || "タグ名を入力してください"],
      auth: [],
      accessToken: null,
    };
  },
  mounted() {
    this.tagId = this.$route.params.tagId;
    this.auth = JSON.parse(sessionStorage.getItem("user"));
    this.accessToken = this.auth.accessToken;
    this.getTag();
  },
  methods: {
    async getTag() {
      await this.axios
        .get("http://0.0.0.0:8000/api/tag/" + this.tagId + "/", {
          headers: { Authorization: "JWT " + this.accessToken },
        })
        .then((response) => {
          console.log(response);
          this.tag = response.data;
          this.tagName = this.tag.name;
        })
        .catch((e) => {
          console.log("エラー", e);
        });
    },
    async validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        console.log(this.tagName);
        await this.axios
          .put(
            "http://0.0.0.0:8000/api/tag/" + this.tagId + "/",
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
            console.log("タグの更新に失敗しました", e);
          });
      }
    },
    async deleteTag() {
      await this.axios
        .delete("http://0.0.0.0:8000/api/tag/" + this.tagId + "/", {
          headers: { Authorization: "JWT " + this.accessToken },
        })
        .then((response) => {
          console.log(response);
          this.$router.push("/tag");
        })
        .catch((e) => {
          console.log("タグ削除に失敗しました", e);
        });
    },
  },
};
</script>