<template>
  <v-app id="inspire">
    <AppBar />
    <v-main class="grey lighten-2">
      <v-container>
        <h1>日報作成</h1>
        <v-container>
          <v-row>
            <v-col cols="10" class="white">
              <v-form ref="form" v-model="valid" lazy-validation class="ml-10">
                <v-menu
                  ref="menu"
                  v-model="menu"
                  :close-on-content-click="false"
                  :return-value.sync="date"
                  transition="scale-transition"
                  offset-y
                  min-width="auto"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="date"
                      label="対象日"
                      prepend-icon="mdi-calendar"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker
                    v-model="date"
                    no-title
                    scrollable
                    locale="ja-jp"
                  >
                    <v-spacer></v-spacer>
                    <v-btn text color="primary" @click="menu = false">
                      Cancel
                    </v-btn>
                    <v-btn text color="primary" @click="$refs.menu.save(date)">
                      OK
                    </v-btn>
                  </v-date-picker>
                </v-menu>
                <v-combobox
                  v-model="select"
                  :items="tags"
                  item-text="name"
                  label="タグ"
                  multiple
                  chips
                ></v-combobox>
                <v-container fluid>
                  <v-textarea label="内容" auto-grow></v-textarea>
                </v-container>
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
  name: "CreateReport",
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
      date: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
        .toISOString()
        .substr(0, 10),
      menu: null,
      select: [],
      tags: [],
    };
  },
  mounted() {
    this.auth = JSON.parse(sessionStorage.getItem("user"));
    this.accessToken = this.auth.accessToken;
    console.log(this.accessToken);
    this.getTags();
  },
  methods: {
    async getTags() {
      await this.axios
        .get("http://0.0.0.0:8000/api/tag/index/", {
          headers: { Authorization: "JWT " + this.accessToken },
        })
        .then((response) => {
          console.log(response.data);
          this.tags = response.data
        })
        .catch((e) => {
          console.log("エラー", e);
        });
    },
    async validate() {
      this.$refs.form.validate();
      // if (this.$refs.form.validate()) {
      //   console.log(this.tagName);
      //   await this.axios
      //     .post(
      //       "http://0.0.0.0:8000/api/tag/index/",
      //       {
      //         name: this.tagName,
      //       },
      //       { headers: { Authorization: "JWT " + this.accessToken } }
      //     )
      //     .then((response) => {
      //       console.log(response);
      //       this.tagName = "";
      //     })
      //     .catch((e) => {
      //       console.log("タグ作成に失敗しました", e);
      //     });
      // }
    },
  },
  computed: {},
};
</script>