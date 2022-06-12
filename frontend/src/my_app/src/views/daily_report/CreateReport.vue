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
                <v-container fluid>
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
                      <v-btn
                        text
                        color="primary"
                        @click="$refs.menu.save(date)"
                      >
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
                  <v-text-field v-model="notice" label="気付き"></v-text-field>
                  <v-textarea
                    label="内容"
                    auto-grow
                    :rules="contentRules"
                    v-model="content"
                  ></v-textarea>
                </v-container>
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
  name: "CreateReport",
  components: {
    AppBar,
  },
  data() {
    return {
      tagName: "",
      valid: true,
      contentRules: [(v) => !!v || "内容を入力してください"],
      auth: [],
      accessToken: null,
      date: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
        .toISOString()
        .substr(0, 10),
      menu: null,
      select: [],
      tags: [],
      userId: null,
      content: null,
      notice: null,
    };
  },
  mounted() {
    this.auth = JSON.parse(sessionStorage.getItem("user"));
    this.accessToken = this.auth.accessToken;
    this.userId = this.auth.id;
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
          this.tags = response.data;
        })
        .catch((e) => {
          console.log("エラー", e);
        });
    },
    async validate() {
      console.log(this.date);
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        console.log(this.tags)
        // let tagsId = this.tags.map((tag) => tag.id);
        await this.axios
          .post(
            "http://0.0.0.0:8000/api/daily_report/index/",
            {
              user: this.userId,
              tags: this.select,
              content: this.content,
              notice: this.notice,
              target_date: this.date,
            },
            { headers: { Authorization: "JWT " + this.accessToken } }
          )
          .then((response) => {
            console.log(response);
          })
          .catch((e) => {
            console.log("日報作成に失敗しました", e);
            console.log(e.request);
          });
      }
    },
  },
  computed: {},
};
</script>