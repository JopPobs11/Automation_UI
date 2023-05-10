from src.tools import environment as ut
import allure_commons



@allure_commons.fixture
def before_all(context):
    ut.do_before_all(context)


@allure_commons.fixture
def after_all(context):
    ut.do_after_all(context)


@allure_commons.fixture
def before_feature(context,feature):
    ut.do_before_feature(context,feature)


@allure_commons.fixture
def after_feature(context,feature):
    ut.do_after_feature(context,feature)


@allure_commons.fixture
def before_scenario(context,scenario):
    ut.do_before_scenario(context, scenario)


@allure_commons.fixture
def after_scenario(context,scenario):
    ut.do_after_scenario(context,scenario)


@allure_commons.fixture
def before_step(context, step):
    ut.do_before_step(context, step)


@allure_commons.fixture
def after_step(context, step):
    ut.do_after_step(context, step)
    
    
@allure_commons.fixture
def before_tag(context, tag):
    ut.do_before_tag(context, tag)


@allure_commons.fixture    
def after_tag(context, tag):
    ut.do_after_tag(context, tag)
    
    


