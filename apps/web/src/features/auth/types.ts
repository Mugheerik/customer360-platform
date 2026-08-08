export interface LoginCredentials {
  email: string;
  password: string;
}

export interface AuthUser {
  id: string;
  email: string;
  is_active: boolean;
  is_superuser: boolean;
}

export interface AuthToken {
  access_token: string;
  token_type: string;
}