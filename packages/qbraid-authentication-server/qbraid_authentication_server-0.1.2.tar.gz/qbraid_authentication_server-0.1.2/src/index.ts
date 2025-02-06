import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

// import { requestAPI } from './handler';

/**
 * Initialization data for the @qbraid/authentication-server extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: '@qbraid/authentication-server:plugin',
  description:
    'A JupyterLab extension. used to get the user credentials from qbraidrc file, with the support of qbraid-core module.',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    console.log(
      'JupyterLab extension @qbraid/authentication-server is activated!'
    );

    // requestAPI<any>('get-example')
    //   .then(data => {
    //     console.log(data);
    //   })
    //   .catch(reason => {
    //     console.error(
    //       `The qbraid_authentication_server server extension appears to be missing.\n${reason}`
    //     );
    //   });
  }
};

export default plugin;
