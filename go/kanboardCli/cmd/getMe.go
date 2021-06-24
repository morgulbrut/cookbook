/*
Copyright © 2021 NAME HERE <EMAIL ADDRESS>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
package cmd

import (
	"encoding/json"
	"fmt"
	"log"
	"strings"

	"github.com/spf13/cobra"
)

type User struct {
	ID         int64  `json:"id"`
	Jsonrpc    string `json:"jsonrpc"`
	UserResult struct {
		APIAccessToken       string      `json:"api_access_token"`
		AvatarPath           string      `json:"avatar_path"`
		DisableLoginForm     string      `json:"disable_login_form"`
		Email                interface{} `json:"email"`
		Filter               interface{} `json:"filter"`
		GithubID             interface{} `json:"github_id"`
		GitlabID             interface{} `json:"gitlab_id"`
		GoogleID             interface{} `json:"google_id"`
		ID                   int64       `json:"id"`
		IsActive             string      `json:"is_active"`
		IsLdapUser           bool        `json:"is_ldap_user"`
		Language             interface{} `json:"language"`
		LockExpirationDate   string      `json:"lock_expiration_date"`
		Name                 interface{} `json:"name"`
		NbFailedLogin        string      `json:"nb_failed_login"`
		NotificationsEnabled string      `json:"notifications_enabled"`
		NotificationsFilter  string      `json:"notifications_filter"`
		Role                 string      `json:"role"`
		Timezone             interface{} `json:"timezone"`
		Token                string      `json:"token"`
		TwofactorActivated   bool        `json:"twofactor_activated"`
		TwofactorSecret      interface{} `json:"twofactor_secret"`
		Username             string      `json:"username"`
	} `json:"result"`
}

// getMeCmd represents the getMe command
var getMeCmd = &cobra.Command{
	Use:   "getMe",
	Short: "Prints the user data for user <ID>",
	Run: func(cmd *cobra.Command, args []string) {
		dat, err := getMe(args[0])
		if err != nil {
			log.Fatal(err)
		}
		empJSON, err := json.MarshalIndent(dat, "", "  ")
		if err != nil {
			log.Fatalf(err.Error())
		}
		fmt.Printf("User\n %s\n", string(empJSON))
	},
}

var usernameCmd = &cobra.Command{
	Use:   "username",
	Short: "Prints the username for user <ID>",
	Run: func(cmd *cobra.Command, args []string) {
		dat, err := getMe(args[0])
		if err != nil {
			log.Fatal(err)
		}

		fmt.Println(dat.UserResult.Username)
	},
}

func getMe(id string) (User, error) {
	var dat User
	var data = strings.NewReader(fmt.Sprintf(`{"jsonrpc": "2.0", "method": "getMe", "id": %s}`, id))
	resp, err := Request(data)
	if err != nil {
		return User{}, err
	}
	if err := json.Unmarshal(resp, &dat); err != nil {
		return User{}, err
	}
	return dat, nil
}

func init() {
	rootCmd.AddCommand(getMeCmd)
	getMeCmd.AddCommand(usernameCmd)
}
