import pytest

from httptest.endpoints.jsonplaceholder import (
    CreatePost,
    DeletePost,
    GetPost,
    GetPostComments,
    GetPosts,
    PatchPost,
    UpdatePost,
)
from httptest.utils.validate import Base, param_id
from params.jsonplaceholder import (
    create_post_params,
    delete_post_params,
    get_post_negative_params,
    get_post_params,
    patch_post_params,
    update_post_params,
)


class TestGetPosts(Base):
    def test_get_posts(self):
        self.response = GetPosts()
        self.validate()


class TestGetPost(Base):
    @pytest.mark.parametrize("params", get_post_params, ids=param_id)
    def test_get_post(self, params):
        self.response = GetPost(**params)
        self.validate()

    @pytest.mark.parametrize("params", get_post_negative_params, ids=param_id)
    def test_get_post_negative(self, params):
        self.response = GetPost(**params)
        self.validate(case="negative")


class TestGetPostComments(Base):
    @pytest.mark.parametrize("params", get_post_params, ids=param_id)
    def test_get_post_comments(self, params):
        self.response = GetPostComments(**params)
        self.validate()


class TestCreatePost(Base):
    @pytest.mark.parametrize("params", create_post_params, ids=param_id)
    def test_create_post(self, params):
        self.response = CreatePost(**params)
        self.validate(status_code=201)


class TestUpdatePost(Base):
    @pytest.mark.parametrize("params", update_post_params, ids=param_id)
    def test_update_post(self, params):
        self.response = UpdatePost(**params)
        self.validate()


class TestPatchPost(Base):
    @pytest.mark.parametrize("params", patch_post_params, ids=param_id)
    def test_patch_post(self, params):
        self.response = PatchPost(**params)
        self.validate()


class TestDeletePost(Base):
    @pytest.mark.parametrize("params", delete_post_params, ids=param_id)
    def test_delete_post(self, params):
        self.response = DeletePost(**params)
        self.validate()
