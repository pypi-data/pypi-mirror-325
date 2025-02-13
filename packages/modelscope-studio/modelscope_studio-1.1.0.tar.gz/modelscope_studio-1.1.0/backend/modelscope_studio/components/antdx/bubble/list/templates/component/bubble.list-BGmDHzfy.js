import { i as Wt, a as Le, r as Ut, g as Gt, w as ae, c as Y, b as Kt } from "./Index-yOhMF7Np.js";
const I = window.ms_globals.React, g = window.ms_globals.React, ke = window.ms_globals.React.useMemo, Ft = window.ms_globals.React.forwardRef, Xt = window.ms_globals.React.useRef, Nt = window.ms_globals.React.useState, Vt = window.ms_globals.React.useEffect, je = window.ms_globals.ReactDOM.createPortal, qt = window.ms_globals.internalContext.useContextPropsContext, Ke = window.ms_globals.internalContext.ContextPropsProvider, bt = window.ms_globals.createItemsContext.createItemsContext, Yt = window.ms_globals.antd.ConfigProvider, $e = window.ms_globals.antd.theme, Qt = window.ms_globals.antd.Avatar, re = window.ms_globals.antdCssinjs.unit, Ee = window.ms_globals.antdCssinjs.token2CSSVar, qe = window.ms_globals.antdCssinjs.useStyleRegister, Jt = window.ms_globals.antdCssinjs.useCSSVarRegister, Zt = window.ms_globals.antdCssinjs.createTheme, en = window.ms_globals.antdCssinjs.useCacheToken, yt = window.ms_globals.antdCssinjs.Keyframes;
var tn = /\s/;
function nn(t) {
  for (var e = t.length; e-- && tn.test(t.charAt(e)); )
    ;
  return e;
}
var rn = /^\s+/;
function on(t) {
  return t && t.slice(0, nn(t) + 1).replace(rn, "");
}
var Ye = NaN, sn = /^[-+]0x[0-9a-f]+$/i, an = /^0b[01]+$/i, ln = /^0o[0-7]+$/i, cn = parseInt;
function Qe(t) {
  if (typeof t == "number")
    return t;
  if (Wt(t))
    return Ye;
  if (Le(t)) {
    var e = typeof t.valueOf == "function" ? t.valueOf() : t;
    t = Le(e) ? e + "" : e;
  }
  if (typeof t != "string")
    return t === 0 ? t : +t;
  t = on(t);
  var r = an.test(t);
  return r || ln.test(t) ? cn(t.slice(2), r ? 2 : 8) : sn.test(t) ? Ye : +t;
}
var Me = function() {
  return Ut.Date.now();
}, un = "Expected a function", fn = Math.max, dn = Math.min;
function hn(t, e, r) {
  var o, n, s, i, a, l, u = 0, f = !1, c = !1, d = !0;
  if (typeof t != "function")
    throw new TypeError(un);
  e = Qe(e) || 0, Le(r) && (f = !!r.leading, c = "maxWait" in r, s = c ? fn(Qe(r.maxWait) || 0, e) : s, d = "trailing" in r ? !!r.trailing : d);
  function m(C) {
    var M = o, O = n;
    return o = n = void 0, u = C, i = t.apply(O, M), i;
  }
  function v(C) {
    return u = C, a = setTimeout(y, e), f ? m(C) : i;
  }
  function h(C) {
    var M = C - l, O = C - u, S = e - M;
    return c ? dn(S, s - O) : S;
  }
  function b(C) {
    var M = C - l, O = C - u;
    return l === void 0 || M >= e || M < 0 || c && O >= s;
  }
  function y() {
    var C = Me();
    if (b(C))
      return E(C);
    a = setTimeout(y, h(C));
  }
  function E(C) {
    return a = void 0, d && o ? m(C) : (o = n = void 0, i);
  }
  function k() {
    a !== void 0 && clearTimeout(a), u = 0, o = l = n = a = void 0;
  }
  function p() {
    return a === void 0 ? i : E(Me());
  }
  function x() {
    var C = Me(), M = b(C);
    if (o = arguments, n = this, l = C, M) {
      if (a === void 0)
        return v(l);
      if (c)
        return clearTimeout(a), a = setTimeout(y, e), m(l);
    }
    return a === void 0 && (a = setTimeout(y, e)), i;
  }
  return x.cancel = k, x.flush = p, x;
}
var vt = {
  exports: {}
}, he = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var gn = g, pn = Symbol.for("react.element"), mn = Symbol.for("react.fragment"), bn = Object.prototype.hasOwnProperty, yn = gn.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, vn = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function St(t, e, r) {
  var o, n = {}, s = null, i = null;
  r !== void 0 && (s = "" + r), e.key !== void 0 && (s = "" + e.key), e.ref !== void 0 && (i = e.ref);
  for (o in e) bn.call(e, o) && !vn.hasOwnProperty(o) && (n[o] = e[o]);
  if (t && t.defaultProps) for (o in e = t.defaultProps, e) n[o] === void 0 && (n[o] = e[o]);
  return {
    $$typeof: pn,
    type: t,
    key: s,
    ref: i,
    props: n,
    _owner: yn.current
  };
}
he.Fragment = mn;
he.jsx = St;
he.jsxs = St;
vt.exports = he;
var G = vt.exports;
const {
  SvelteComponent: Sn,
  assign: Je,
  binding_callbacks: Ze,
  check_outros: xn,
  children: xt,
  claim_element: Ct,
  claim_space: Cn,
  component_subscribe: et,
  compute_slots: wn,
  create_slot: _n,
  detach: Q,
  element: wt,
  empty: tt,
  exclude_internal_props: nt,
  get_all_dirty_from_scope: Tn,
  get_slot_changes: En,
  group_outros: Mn,
  init: On,
  insert_hydration: le,
  safe_not_equal: Pn,
  set_custom_element_data: _t,
  space: In,
  transition_in: ce,
  transition_out: De,
  update_slot_base: Rn
} = window.__gradio__svelte__internal, {
  beforeUpdate: kn,
  getContext: jn,
  onDestroy: Ln,
  setContext: $n
} = window.__gradio__svelte__internal;
function rt(t) {
  let e, r;
  const o = (
    /*#slots*/
    t[7].default
  ), n = _n(
    o,
    t,
    /*$$scope*/
    t[6],
    null
  );
  return {
    c() {
      e = wt("svelte-slot"), n && n.c(), this.h();
    },
    l(s) {
      e = Ct(s, "SVELTE-SLOT", {
        class: !0
      });
      var i = xt(e);
      n && n.l(i), i.forEach(Q), this.h();
    },
    h() {
      _t(e, "class", "svelte-1rt0kpf");
    },
    m(s, i) {
      le(s, e, i), n && n.m(e, null), t[9](e), r = !0;
    },
    p(s, i) {
      n && n.p && (!r || i & /*$$scope*/
      64) && Rn(
        n,
        o,
        s,
        /*$$scope*/
        s[6],
        r ? En(
          o,
          /*$$scope*/
          s[6],
          i,
          null
        ) : Tn(
          /*$$scope*/
          s[6]
        ),
        null
      );
    },
    i(s) {
      r || (ce(n, s), r = !0);
    },
    o(s) {
      De(n, s), r = !1;
    },
    d(s) {
      s && Q(e), n && n.d(s), t[9](null);
    }
  };
}
function Dn(t) {
  let e, r, o, n, s = (
    /*$$slots*/
    t[4].default && rt(t)
  );
  return {
    c() {
      e = wt("react-portal-target"), r = In(), s && s.c(), o = tt(), this.h();
    },
    l(i) {
      e = Ct(i, "REACT-PORTAL-TARGET", {
        class: !0
      }), xt(e).forEach(Q), r = Cn(i), s && s.l(i), o = tt(), this.h();
    },
    h() {
      _t(e, "class", "svelte-1rt0kpf");
    },
    m(i, a) {
      le(i, e, a), t[8](e), le(i, r, a), s && s.m(i, a), le(i, o, a), n = !0;
    },
    p(i, [a]) {
      /*$$slots*/
      i[4].default ? s ? (s.p(i, a), a & /*$$slots*/
      16 && ce(s, 1)) : (s = rt(i), s.c(), ce(s, 1), s.m(o.parentNode, o)) : s && (Mn(), De(s, 1, 1, () => {
        s = null;
      }), xn());
    },
    i(i) {
      n || (ce(s), n = !0);
    },
    o(i) {
      De(s), n = !1;
    },
    d(i) {
      i && (Q(e), Q(r), Q(o)), t[8](null), s && s.d(i);
    }
  };
}
function ot(t) {
  const {
    svelteInit: e,
    ...r
  } = t;
  return r;
}
function Hn(t, e, r) {
  let o, n, {
    $$slots: s = {},
    $$scope: i
  } = e;
  const a = wn(s);
  let {
    svelteInit: l
  } = e;
  const u = ae(ot(e)), f = ae();
  et(t, f, (p) => r(0, o = p));
  const c = ae();
  et(t, c, (p) => r(1, n = p));
  const d = [], m = jn("$$ms-gr-react-wrapper"), {
    slotKey: v,
    slotIndex: h,
    subSlotIndex: b
  } = Gt() || {}, y = l({
    parent: m,
    props: u,
    target: f,
    slot: c,
    slotKey: v,
    slotIndex: h,
    subSlotIndex: b,
    onDestroy(p) {
      d.push(p);
    }
  });
  $n("$$ms-gr-react-wrapper", y), kn(() => {
    u.set(ot(e));
  }), Ln(() => {
    d.forEach((p) => p());
  });
  function E(p) {
    Ze[p ? "unshift" : "push"](() => {
      o = p, f.set(o);
    });
  }
  function k(p) {
    Ze[p ? "unshift" : "push"](() => {
      n = p, c.set(n);
    });
  }
  return t.$$set = (p) => {
    r(17, e = Je(Je({}, e), nt(p))), "svelteInit" in p && r(5, l = p.svelteInit), "$$scope" in p && r(6, i = p.$$scope);
  }, e = nt(e), [o, n, f, c, a, l, i, s, E, k];
}
class Bn extends Sn {
  constructor(e) {
    super(), On(this, e, Hn, Dn, Pn, {
      svelteInit: 5
    });
  }
}
const st = window.ms_globals.rerender, Oe = window.ms_globals.tree;
function zn(t, e = {}) {
  function r(o) {
    const n = ae(), s = new Bn({
      ...o,
      props: {
        svelteInit(i) {
          window.ms_globals.autokey += 1;
          const a = {
            key: window.ms_globals.autokey,
            svelteInstance: n,
            reactComponent: t,
            props: i.props,
            slot: i.slot,
            target: i.target,
            slotIndex: i.slotIndex,
            subSlotIndex: i.subSlotIndex,
            ignore: e.ignore,
            slotKey: i.slotKey,
            nodes: []
          }, l = i.parent ?? Oe;
          return l.nodes = [...l.nodes, a], st({
            createPortal: je,
            node: Oe
          }), i.onDestroy(() => {
            l.nodes = l.nodes.filter((u) => u.svelteInstance !== n), st({
              createPortal: je,
              node: Oe
            });
          }), a;
        },
        ...o.props
      }
    });
    return n.set(s), s;
  }
  return new Promise((o) => {
    window.ms_globals.initializePromise.then(() => {
      o(r);
    });
  });
}
const An = "1.0.5", Fn = /* @__PURE__ */ g.createContext({}), Xn = {
  classNames: {},
  styles: {},
  className: "",
  style: {}
}, Nn = (t) => {
  const e = g.useContext(Fn);
  return g.useMemo(() => ({
    ...Xn,
    ...e[t]
  }), [e[t]]);
};
function oe() {
  return oe = Object.assign ? Object.assign.bind() : function(t) {
    for (var e = 1; e < arguments.length; e++) {
      var r = arguments[e];
      for (var o in r) ({}).hasOwnProperty.call(r, o) && (t[o] = r[o]);
    }
    return t;
  }, oe.apply(null, arguments);
}
function fe() {
  const {
    getPrefixCls: t,
    direction: e,
    csp: r,
    iconPrefixCls: o,
    theme: n
  } = g.useContext(Yt.ConfigContext);
  return {
    theme: n,
    getPrefixCls: t,
    direction: e,
    csp: r,
    iconPrefixCls: o
  };
}
function Tt(t) {
  var e = I.useRef();
  e.current = t;
  var r = I.useCallback(function() {
    for (var o, n = arguments.length, s = new Array(n), i = 0; i < n; i++)
      s[i] = arguments[i];
    return (o = e.current) === null || o === void 0 ? void 0 : o.call.apply(o, [e].concat(s));
  }, []);
  return r;
}
function Vn(t) {
  if (Array.isArray(t)) return t;
}
function Wn(t, e) {
  var r = t == null ? null : typeof Symbol < "u" && t[Symbol.iterator] || t["@@iterator"];
  if (r != null) {
    var o, n, s, i, a = [], l = !0, u = !1;
    try {
      if (s = (r = r.call(t)).next, e === 0) {
        if (Object(r) !== r) return;
        l = !1;
      } else for (; !(l = (o = s.call(r)).done) && (a.push(o.value), a.length !== e); l = !0) ;
    } catch (f) {
      u = !0, n = f;
    } finally {
      try {
        if (!l && r.return != null && (i = r.return(), Object(i) !== i)) return;
      } finally {
        if (u) throw n;
      }
    }
    return a;
  }
}
function it(t, e) {
  (e == null || e > t.length) && (e = t.length);
  for (var r = 0, o = Array(e); r < e; r++) o[r] = t[r];
  return o;
}
function Un(t, e) {
  if (t) {
    if (typeof t == "string") return it(t, e);
    var r = {}.toString.call(t).slice(8, -1);
    return r === "Object" && t.constructor && (r = t.constructor.name), r === "Map" || r === "Set" ? Array.from(t) : r === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r) ? it(t, e) : void 0;
  }
}
function Gn() {
  throw new TypeError(`Invalid attempt to destructure non-iterable instance.
In order to be iterable, non-array objects must have a [Symbol.iterator]() method.`);
}
function ue(t, e) {
  return Vn(t) || Wn(t, e) || Un(t, e) || Gn();
}
function Kn() {
  return !!(typeof window < "u" && window.document && window.document.createElement);
}
var at = Kn() ? I.useLayoutEffect : I.useEffect, qn = function(e, r) {
  var o = I.useRef(!0);
  at(function() {
    return e(o.current);
  }, r), at(function() {
    return o.current = !1, function() {
      o.current = !0;
    };
  }, []);
};
function X(t) {
  "@babel/helpers - typeof";
  return X = typeof Symbol == "function" && typeof Symbol.iterator == "symbol" ? function(e) {
    return typeof e;
  } : function(e) {
    return e && typeof Symbol == "function" && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e;
  }, X(t);
}
var T = {};
/**
 * @license React
 * react-is.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Fe = Symbol.for("react.element"), Xe = Symbol.for("react.portal"), ge = Symbol.for("react.fragment"), pe = Symbol.for("react.strict_mode"), me = Symbol.for("react.profiler"), be = Symbol.for("react.provider"), ye = Symbol.for("react.context"), Yn = Symbol.for("react.server_context"), ve = Symbol.for("react.forward_ref"), Se = Symbol.for("react.suspense"), xe = Symbol.for("react.suspense_list"), Ce = Symbol.for("react.memo"), we = Symbol.for("react.lazy"), Qn = Symbol.for("react.offscreen"), Et;
Et = Symbol.for("react.module.reference");
function H(t) {
  if (typeof t == "object" && t !== null) {
    var e = t.$$typeof;
    switch (e) {
      case Fe:
        switch (t = t.type, t) {
          case ge:
          case me:
          case pe:
          case Se:
          case xe:
            return t;
          default:
            switch (t = t && t.$$typeof, t) {
              case Yn:
              case ye:
              case ve:
              case we:
              case Ce:
              case be:
                return t;
              default:
                return e;
            }
        }
      case Xe:
        return e;
    }
  }
}
T.ContextConsumer = ye;
T.ContextProvider = be;
T.Element = Fe;
T.ForwardRef = ve;
T.Fragment = ge;
T.Lazy = we;
T.Memo = Ce;
T.Portal = Xe;
T.Profiler = me;
T.StrictMode = pe;
T.Suspense = Se;
T.SuspenseList = xe;
T.isAsyncMode = function() {
  return !1;
};
T.isConcurrentMode = function() {
  return !1;
};
T.isContextConsumer = function(t) {
  return H(t) === ye;
};
T.isContextProvider = function(t) {
  return H(t) === be;
};
T.isElement = function(t) {
  return typeof t == "object" && t !== null && t.$$typeof === Fe;
};
T.isForwardRef = function(t) {
  return H(t) === ve;
};
T.isFragment = function(t) {
  return H(t) === ge;
};
T.isLazy = function(t) {
  return H(t) === we;
};
T.isMemo = function(t) {
  return H(t) === Ce;
};
T.isPortal = function(t) {
  return H(t) === Xe;
};
T.isProfiler = function(t) {
  return H(t) === me;
};
T.isStrictMode = function(t) {
  return H(t) === pe;
};
T.isSuspense = function(t) {
  return H(t) === Se;
};
T.isSuspenseList = function(t) {
  return H(t) === xe;
};
T.isValidElementType = function(t) {
  return typeof t == "string" || typeof t == "function" || t === ge || t === me || t === pe || t === Se || t === xe || t === Qn || typeof t == "object" && t !== null && (t.$$typeof === we || t.$$typeof === Ce || t.$$typeof === be || t.$$typeof === ye || t.$$typeof === ve || t.$$typeof === Et || t.getModuleId !== void 0);
};
T.typeOf = H;
function Jn(t, e) {
  if (X(t) != "object" || !t) return t;
  var r = t[Symbol.toPrimitive];
  if (r !== void 0) {
    var o = r.call(t, e || "default");
    if (X(o) != "object") return o;
    throw new TypeError("@@toPrimitive must return a primitive value.");
  }
  return (e === "string" ? String : Number)(t);
}
function Mt(t) {
  var e = Jn(t, "string");
  return X(e) == "symbol" ? e : e + "";
}
function R(t, e, r) {
  return (e = Mt(e)) in t ? Object.defineProperty(t, e, {
    value: r,
    enumerable: !0,
    configurable: !0,
    writable: !0
  }) : t[e] = r, t;
}
function lt(t, e) {
  var r = Object.keys(t);
  if (Object.getOwnPropertySymbols) {
    var o = Object.getOwnPropertySymbols(t);
    e && (o = o.filter(function(n) {
      return Object.getOwnPropertyDescriptor(t, n).enumerable;
    })), r.push.apply(r, o);
  }
  return r;
}
function D(t) {
  for (var e = 1; e < arguments.length; e++) {
    var r = arguments[e] != null ? arguments[e] : {};
    e % 2 ? lt(Object(r), !0).forEach(function(o) {
      R(t, o, r[o]);
    }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(t, Object.getOwnPropertyDescriptors(r)) : lt(Object(r)).forEach(function(o) {
      Object.defineProperty(t, o, Object.getOwnPropertyDescriptor(r, o));
    });
  }
  return t;
}
function _e(t, e) {
  if (!(t instanceof e)) throw new TypeError("Cannot call a class as a function");
}
function Zn(t, e) {
  for (var r = 0; r < e.length; r++) {
    var o = e[r];
    o.enumerable = o.enumerable || !1, o.configurable = !0, "value" in o && (o.writable = !0), Object.defineProperty(t, Mt(o.key), o);
  }
}
function Te(t, e, r) {
  return e && Zn(t.prototype, e), Object.defineProperty(t, "prototype", {
    writable: !1
  }), t;
}
function He(t, e) {
  return He = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function(r, o) {
    return r.__proto__ = o, r;
  }, He(t, e);
}
function Ot(t, e) {
  if (typeof e != "function" && e !== null) throw new TypeError("Super expression must either be null or a function");
  t.prototype = Object.create(e && e.prototype, {
    constructor: {
      value: t,
      writable: !0,
      configurable: !0
    }
  }), Object.defineProperty(t, "prototype", {
    writable: !1
  }), e && He(t, e);
}
function de(t) {
  return de = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function(e) {
    return e.__proto__ || Object.getPrototypeOf(e);
  }, de(t);
}
function Pt() {
  try {
    var t = !Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function() {
    }));
  } catch {
  }
  return (Pt = function() {
    return !!t;
  })();
}
function ne(t) {
  if (t === void 0) throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
  return t;
}
function er(t, e) {
  if (e && (X(e) == "object" || typeof e == "function")) return e;
  if (e !== void 0) throw new TypeError("Derived constructors may only return object or undefined");
  return ne(t);
}
function It(t) {
  var e = Pt();
  return function() {
    var r, o = de(t);
    if (e) {
      var n = de(this).constructor;
      r = Reflect.construct(o, arguments, n);
    } else r = o.apply(this, arguments);
    return er(this, r);
  };
}
var Rt = /* @__PURE__ */ Te(function t() {
  _e(this, t);
}), kt = "CALC_UNIT", tr = new RegExp(kt, "g");
function Pe(t) {
  return typeof t == "number" ? "".concat(t).concat(kt) : t;
}
var nr = /* @__PURE__ */ function(t) {
  Ot(r, t);
  var e = It(r);
  function r(o, n) {
    var s;
    _e(this, r), s = e.call(this), R(ne(s), "result", ""), R(ne(s), "unitlessCssVar", void 0), R(ne(s), "lowPriority", void 0);
    var i = X(o);
    return s.unitlessCssVar = n, o instanceof r ? s.result = "(".concat(o.result, ")") : i === "number" ? s.result = Pe(o) : i === "string" && (s.result = o), s;
  }
  return Te(r, [{
    key: "add",
    value: function(n) {
      return n instanceof r ? this.result = "".concat(this.result, " + ").concat(n.getResult()) : (typeof n == "number" || typeof n == "string") && (this.result = "".concat(this.result, " + ").concat(Pe(n))), this.lowPriority = !0, this;
    }
  }, {
    key: "sub",
    value: function(n) {
      return n instanceof r ? this.result = "".concat(this.result, " - ").concat(n.getResult()) : (typeof n == "number" || typeof n == "string") && (this.result = "".concat(this.result, " - ").concat(Pe(n))), this.lowPriority = !0, this;
    }
  }, {
    key: "mul",
    value: function(n) {
      return this.lowPriority && (this.result = "(".concat(this.result, ")")), n instanceof r ? this.result = "".concat(this.result, " * ").concat(n.getResult(!0)) : (typeof n == "number" || typeof n == "string") && (this.result = "".concat(this.result, " * ").concat(n)), this.lowPriority = !1, this;
    }
  }, {
    key: "div",
    value: function(n) {
      return this.lowPriority && (this.result = "(".concat(this.result, ")")), n instanceof r ? this.result = "".concat(this.result, " / ").concat(n.getResult(!0)) : (typeof n == "number" || typeof n == "string") && (this.result = "".concat(this.result, " / ").concat(n)), this.lowPriority = !1, this;
    }
  }, {
    key: "getResult",
    value: function(n) {
      return this.lowPriority || n ? "(".concat(this.result, ")") : this.result;
    }
  }, {
    key: "equal",
    value: function(n) {
      var s = this, i = n || {}, a = i.unit, l = !0;
      return typeof a == "boolean" ? l = a : Array.from(this.unitlessCssVar).some(function(u) {
        return s.result.includes(u);
      }) && (l = !1), this.result = this.result.replace(tr, l ? "px" : ""), typeof this.lowPriority < "u" ? "calc(".concat(this.result, ")") : this.result;
    }
  }]), r;
}(Rt), rr = /* @__PURE__ */ function(t) {
  Ot(r, t);
  var e = It(r);
  function r(o) {
    var n;
    return _e(this, r), n = e.call(this), R(ne(n), "result", 0), o instanceof r ? n.result = o.result : typeof o == "number" && (n.result = o), n;
  }
  return Te(r, [{
    key: "add",
    value: function(n) {
      return n instanceof r ? this.result += n.result : typeof n == "number" && (this.result += n), this;
    }
  }, {
    key: "sub",
    value: function(n) {
      return n instanceof r ? this.result -= n.result : typeof n == "number" && (this.result -= n), this;
    }
  }, {
    key: "mul",
    value: function(n) {
      return n instanceof r ? this.result *= n.result : typeof n == "number" && (this.result *= n), this;
    }
  }, {
    key: "div",
    value: function(n) {
      return n instanceof r ? this.result /= n.result : typeof n == "number" && (this.result /= n), this;
    }
  }, {
    key: "equal",
    value: function() {
      return this.result;
    }
  }]), r;
}(Rt), or = function(e, r) {
  var o = e === "css" ? nr : rr;
  return function(n) {
    return new o(n, r);
  };
}, ct = function(e, r) {
  return "".concat([r, e.replace(/([A-Z]+)([A-Z][a-z]+)/g, "$1-$2").replace(/([a-z])([A-Z])/g, "$1-$2")].filter(Boolean).join("-"));
};
function ut(t, e, r, o) {
  var n = D({}, e[t]);
  if (o != null && o.deprecatedTokens) {
    var s = o.deprecatedTokens;
    s.forEach(function(a) {
      var l = ue(a, 2), u = l[0], f = l[1];
      if (n != null && n[u] || n != null && n[f]) {
        var c;
        (c = n[f]) !== null && c !== void 0 || (n[f] = n == null ? void 0 : n[u]);
      }
    });
  }
  var i = D(D({}, r), n);
  return Object.keys(i).forEach(function(a) {
    i[a] === e[a] && delete i[a];
  }), i;
}
var jt = typeof CSSINJS_STATISTIC < "u", Be = !0;
function Ne() {
  for (var t = arguments.length, e = new Array(t), r = 0; r < t; r++)
    e[r] = arguments[r];
  if (!jt)
    return Object.assign.apply(Object, [{}].concat(e));
  Be = !1;
  var o = {};
  return e.forEach(function(n) {
    if (X(n) === "object") {
      var s = Object.keys(n);
      s.forEach(function(i) {
        Object.defineProperty(o, i, {
          configurable: !0,
          enumerable: !0,
          get: function() {
            return n[i];
          }
        });
      });
    }
  }), Be = !0, o;
}
var ft = {};
function sr() {
}
var ir = function(e) {
  var r, o = e, n = sr;
  return jt && typeof Proxy < "u" && (r = /* @__PURE__ */ new Set(), o = new Proxy(e, {
    get: function(i, a) {
      if (Be) {
        var l;
        (l = r) === null || l === void 0 || l.add(a);
      }
      return i[a];
    }
  }), n = function(i, a) {
    var l;
    ft[i] = {
      global: Array.from(r),
      component: D(D({}, (l = ft[i]) === null || l === void 0 ? void 0 : l.component), a)
    };
  }), {
    token: o,
    keys: r,
    flush: n
  };
};
function dt(t, e, r) {
  if (typeof r == "function") {
    var o;
    return r(Ne(e, (o = e[t]) !== null && o !== void 0 ? o : {}));
  }
  return r ?? {};
}
function ar(t) {
  return t === "js" ? {
    max: Math.max,
    min: Math.min
  } : {
    max: function() {
      for (var r = arguments.length, o = new Array(r), n = 0; n < r; n++)
        o[n] = arguments[n];
      return "max(".concat(o.map(function(s) {
        return re(s);
      }).join(","), ")");
    },
    min: function() {
      for (var r = arguments.length, o = new Array(r), n = 0; n < r; n++)
        o[n] = arguments[n];
      return "min(".concat(o.map(function(s) {
        return re(s);
      }).join(","), ")");
    }
  };
}
var lr = 1e3 * 60 * 10, cr = /* @__PURE__ */ function() {
  function t() {
    _e(this, t), R(this, "map", /* @__PURE__ */ new Map()), R(this, "objectIDMap", /* @__PURE__ */ new WeakMap()), R(this, "nextID", 0), R(this, "lastAccessBeat", /* @__PURE__ */ new Map()), R(this, "accessBeat", 0);
  }
  return Te(t, [{
    key: "set",
    value: function(r, o) {
      this.clear();
      var n = this.getCompositeKey(r);
      this.map.set(n, o), this.lastAccessBeat.set(n, Date.now());
    }
  }, {
    key: "get",
    value: function(r) {
      var o = this.getCompositeKey(r), n = this.map.get(o);
      return this.lastAccessBeat.set(o, Date.now()), this.accessBeat += 1, n;
    }
  }, {
    key: "getCompositeKey",
    value: function(r) {
      var o = this, n = r.map(function(s) {
        return s && X(s) === "object" ? "obj_".concat(o.getObjectID(s)) : "".concat(X(s), "_").concat(s);
      });
      return n.join("|");
    }
  }, {
    key: "getObjectID",
    value: function(r) {
      if (this.objectIDMap.has(r))
        return this.objectIDMap.get(r);
      var o = this.nextID;
      return this.objectIDMap.set(r, o), this.nextID += 1, o;
    }
  }, {
    key: "clear",
    value: function() {
      var r = this;
      if (this.accessBeat > 1e4) {
        var o = Date.now();
        this.lastAccessBeat.forEach(function(n, s) {
          o - n > lr && (r.map.delete(s), r.lastAccessBeat.delete(s));
        }), this.accessBeat = 0;
      }
    }
  }]), t;
}(), ht = new cr();
function ur(t, e) {
  return g.useMemo(function() {
    var r = ht.get(e);
    if (r)
      return r;
    var o = t();
    return ht.set(e, o), o;
  }, e);
}
var fr = function() {
  return {};
};
function dr(t) {
  var e = t.useCSP, r = e === void 0 ? fr : e, o = t.useToken, n = t.usePrefix, s = t.getResetStyles, i = t.getCommonStyle, a = t.getCompUnitless;
  function l(d, m, v, h) {
    var b = Array.isArray(d) ? d[0] : d;
    function y(O) {
      return "".concat(String(b)).concat(O.slice(0, 1).toUpperCase()).concat(O.slice(1));
    }
    var E = (h == null ? void 0 : h.unitless) || {}, k = typeof a == "function" ? a(d) : {}, p = D(D({}, k), {}, R({}, y("zIndexPopup"), !0));
    Object.keys(E).forEach(function(O) {
      p[y(O)] = E[O];
    });
    var x = D(D({}, h), {}, {
      unitless: p,
      prefixToken: y
    }), C = f(d, m, v, x), M = u(b, v, x);
    return function(O) {
      var S = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : O, P = C(O, S), B = ue(P, 2), L = B[1], z = M(S), w = ue(z, 2), _ = w[0], j = w[1];
      return [_, L, j];
    };
  }
  function u(d, m, v) {
    var h = v.unitless, b = v.injectStyle, y = b === void 0 ? !0 : b, E = v.prefixToken, k = v.ignore, p = function(M) {
      var O = M.rootCls, S = M.cssVar, P = S === void 0 ? {} : S, B = o(), L = B.realToken;
      return Jt({
        path: [d],
        prefix: P.prefix,
        key: P.key,
        unitless: h,
        ignore: k,
        token: L,
        scope: O
      }, function() {
        var z = dt(d, L, m), w = ut(d, L, z, {
          deprecatedTokens: v == null ? void 0 : v.deprecatedTokens
        });
        return Object.keys(z).forEach(function(_) {
          w[E(_)] = w[_], delete w[_];
        }), w;
      }), null;
    }, x = function(M) {
      var O = o(), S = O.cssVar;
      return [function(P) {
        return y && S ? /* @__PURE__ */ g.createElement(g.Fragment, null, /* @__PURE__ */ g.createElement(p, {
          rootCls: M,
          cssVar: S,
          component: d
        }), P) : P;
      }, S == null ? void 0 : S.key];
    };
    return x;
  }
  function f(d, m, v) {
    var h = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {}, b = Array.isArray(d) ? d : [d, d], y = ue(b, 1), E = y[0], k = b.join("-"), p = t.layer || {
      name: "antd"
    };
    return function(x) {
      var C = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : x, M = o(), O = M.theme, S = M.realToken, P = M.hashId, B = M.token, L = M.cssVar, z = n(), w = z.rootPrefixCls, _ = z.iconPrefixCls, j = r(), A = L ? "css" : "js", V = ur(function() {
        var F = /* @__PURE__ */ new Set();
        return L && Object.keys(h.unitless || {}).forEach(function(U) {
          F.add(Ee(U, L.prefix)), F.add(Ee(U, ct(E, L.prefix)));
        }), or(A, F);
      }, [A, E, L == null ? void 0 : L.prefix]), W = ar(A), K = W.max, J = W.min, Z = {
        theme: O,
        token: B,
        hashId: P,
        nonce: function() {
          return j.nonce;
        },
        clientOnly: h.clientOnly,
        layer: p,
        // antd is always at top of styles
        order: h.order || -999
      };
      typeof s == "function" && qe(D(D({}, Z), {}, {
        clientOnly: !1,
        path: ["Shared", w]
      }), function() {
        return s(B, {
          prefix: {
            rootPrefixCls: w,
            iconPrefixCls: _
          },
          csp: j
        });
      });
      var ee = qe(D(D({}, Z), {}, {
        path: [k, x, _]
      }), function() {
        if (h.injectStyle === !1)
          return [];
        var F = ir(B), U = F.token, Ht = F.flush, q = dt(E, S, v), Bt = ".".concat(x), We = ut(E, S, q, {
          deprecatedTokens: h.deprecatedTokens
        });
        L && q && X(q) === "object" && Object.keys(q).forEach(function(Ge) {
          q[Ge] = "var(".concat(Ee(Ge, ct(E, L.prefix)), ")");
        });
        var Ue = Ne(U, {
          componentCls: Bt,
          prefixCls: x,
          iconCls: ".".concat(_),
          antCls: ".".concat(w),
          calc: V,
          // @ts-ignore
          max: K,
          // @ts-ignore
          min: J
        }, L ? q : We), zt = m(Ue, {
          hashId: P,
          prefixCls: x,
          rootPrefixCls: w,
          iconPrefixCls: _
        });
        Ht(E, We);
        var At = typeof i == "function" ? i(Ue, x, C, h.resetFont) : null;
        return [h.resetStyle === !1 ? null : At, zt];
      });
      return [ee, P];
    };
  }
  function c(d, m, v) {
    var h = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {}, b = f(d, m, v, D({
      resetStyle: !1,
      // Sub Style should default after root one
      order: -998
    }, h)), y = function(k) {
      var p = k.prefixCls, x = k.rootCls, C = x === void 0 ? p : x;
      return b(p, C), null;
    };
    return y;
  }
  return {
    genStyleHooks: l,
    genSubStyleComponent: c,
    genComponentStyleHook: f
  };
}
const $ = Math.round;
function Ie(t, e) {
  const r = t.replace(/^[^(]*\((.*)/, "$1").replace(/\).*/, "").match(/\d*\.?\d+%?/g) || [], o = r.map((n) => parseFloat(n));
  for (let n = 0; n < 3; n += 1)
    o[n] = e(o[n] || 0, r[n] || "", n);
  return r[3] ? o[3] = r[3].includes("%") ? o[3] / 100 : o[3] : o[3] = 1, o;
}
const gt = (t, e, r) => r === 0 ? t : t / 100;
function te(t, e) {
  const r = e || 255;
  return t > r ? r : t < 0 ? 0 : t;
}
class N {
  constructor(e) {
    R(this, "isValid", !0), R(this, "r", 0), R(this, "g", 0), R(this, "b", 0), R(this, "a", 1), R(this, "_h", void 0), R(this, "_s", void 0), R(this, "_l", void 0), R(this, "_v", void 0), R(this, "_max", void 0), R(this, "_min", void 0), R(this, "_brightness", void 0);
    function r(o) {
      return o[0] in e && o[1] in e && o[2] in e;
    }
    if (e) if (typeof e == "string") {
      let n = function(s) {
        return o.startsWith(s);
      };
      const o = e.trim();
      /^#?[A-F\d]{3,8}$/i.test(o) ? this.fromHexString(o) : n("rgb") ? this.fromRgbString(o) : n("hsl") ? this.fromHslString(o) : (n("hsv") || n("hsb")) && this.fromHsvString(o);
    } else if (e instanceof N)
      this.r = e.r, this.g = e.g, this.b = e.b, this.a = e.a, this._h = e._h, this._s = e._s, this._l = e._l, this._v = e._v;
    else if (r("rgb"))
      this.r = te(e.r), this.g = te(e.g), this.b = te(e.b), this.a = typeof e.a == "number" ? te(e.a, 1) : 1;
    else if (r("hsl"))
      this.fromHsl(e);
    else if (r("hsv"))
      this.fromHsv(e);
    else
      throw new Error("@ant-design/fast-color: unsupported input " + JSON.stringify(e));
  }
  // ======================= Setter =======================
  setR(e) {
    return this._sc("r", e);
  }
  setG(e) {
    return this._sc("g", e);
  }
  setB(e) {
    return this._sc("b", e);
  }
  setA(e) {
    return this._sc("a", e, 1);
  }
  setHue(e) {
    const r = this.toHsv();
    return r.h = e, this._c(r);
  }
  // ======================= Getter =======================
  /**
   * Returns the perceived luminance of a color, from 0-1.
   * @see http://www.w3.org/TR/2008/REC-WCAG20-20081211/#relativeluminancedef
   */
  getLuminance() {
    function e(s) {
      const i = s / 255;
      return i <= 0.03928 ? i / 12.92 : Math.pow((i + 0.055) / 1.055, 2.4);
    }
    const r = e(this.r), o = e(this.g), n = e(this.b);
    return 0.2126 * r + 0.7152 * o + 0.0722 * n;
  }
  getHue() {
    if (typeof this._h > "u") {
      const e = this.getMax() - this.getMin();
      e === 0 ? this._h = 0 : this._h = $(60 * (this.r === this.getMax() ? (this.g - this.b) / e + (this.g < this.b ? 6 : 0) : this.g === this.getMax() ? (this.b - this.r) / e + 2 : (this.r - this.g) / e + 4));
    }
    return this._h;
  }
  getSaturation() {
    if (typeof this._s > "u") {
      const e = this.getMax() - this.getMin();
      e === 0 ? this._s = 0 : this._s = e / this.getMax();
    }
    return this._s;
  }
  getLightness() {
    return typeof this._l > "u" && (this._l = (this.getMax() + this.getMin()) / 510), this._l;
  }
  getValue() {
    return typeof this._v > "u" && (this._v = this.getMax() / 255), this._v;
  }
  /**
   * Returns the perceived brightness of the color, from 0-255.
   * Note: this is not the b of HSB
   * @see http://www.w3.org/TR/AERT#color-contrast
   */
  getBrightness() {
    return typeof this._brightness > "u" && (this._brightness = (this.r * 299 + this.g * 587 + this.b * 114) / 1e3), this._brightness;
  }
  // ======================== Func ========================
  darken(e = 10) {
    const r = this.getHue(), o = this.getSaturation();
    let n = this.getLightness() - e / 100;
    return n < 0 && (n = 0), this._c({
      h: r,
      s: o,
      l: n,
      a: this.a
    });
  }
  lighten(e = 10) {
    const r = this.getHue(), o = this.getSaturation();
    let n = this.getLightness() + e / 100;
    return n > 1 && (n = 1), this._c({
      h: r,
      s: o,
      l: n,
      a: this.a
    });
  }
  /**
   * Mix the current color a given amount with another color, from 0 to 100.
   * 0 means no mixing (return current color).
   */
  mix(e, r = 50) {
    const o = this._c(e), n = r / 100, s = (a) => (o[a] - this[a]) * n + this[a], i = {
      r: $(s("r")),
      g: $(s("g")),
      b: $(s("b")),
      a: $(s("a") * 100) / 100
    };
    return this._c(i);
  }
  /**
   * Mix the color with pure white, from 0 to 100.
   * Providing 0 will do nothing, providing 100 will always return white.
   */
  tint(e = 10) {
    return this.mix({
      r: 255,
      g: 255,
      b: 255,
      a: 1
    }, e);
  }
  /**
   * Mix the color with pure black, from 0 to 100.
   * Providing 0 will do nothing, providing 100 will always return black.
   */
  shade(e = 10) {
    return this.mix({
      r: 0,
      g: 0,
      b: 0,
      a: 1
    }, e);
  }
  onBackground(e) {
    const r = this._c(e), o = this.a + r.a * (1 - this.a), n = (s) => $((this[s] * this.a + r[s] * r.a * (1 - this.a)) / o);
    return this._c({
      r: n("r"),
      g: n("g"),
      b: n("b"),
      a: o
    });
  }
  // ======================= Status =======================
  isDark() {
    return this.getBrightness() < 128;
  }
  isLight() {
    return this.getBrightness() >= 128;
  }
  // ======================== MISC ========================
  equals(e) {
    return this.r === e.r && this.g === e.g && this.b === e.b && this.a === e.a;
  }
  clone() {
    return this._c(this);
  }
  // ======================= Format =======================
  toHexString() {
    let e = "#";
    const r = (this.r || 0).toString(16);
    e += r.length === 2 ? r : "0" + r;
    const o = (this.g || 0).toString(16);
    e += o.length === 2 ? o : "0" + o;
    const n = (this.b || 0).toString(16);
    if (e += n.length === 2 ? n : "0" + n, typeof this.a == "number" && this.a >= 0 && this.a < 1) {
      const s = $(this.a * 255).toString(16);
      e += s.length === 2 ? s : "0" + s;
    }
    return e;
  }
  /** CSS support color pattern */
  toHsl() {
    return {
      h: this.getHue(),
      s: this.getSaturation(),
      l: this.getLightness(),
      a: this.a
    };
  }
  /** CSS support color pattern */
  toHslString() {
    const e = this.getHue(), r = $(this.getSaturation() * 100), o = $(this.getLightness() * 100);
    return this.a !== 1 ? `hsla(${e},${r}%,${o}%,${this.a})` : `hsl(${e},${r}%,${o}%)`;
  }
  /** Same as toHsb */
  toHsv() {
    return {
      h: this.getHue(),
      s: this.getSaturation(),
      v: this.getValue(),
      a: this.a
    };
  }
  toRgb() {
    return {
      r: this.r,
      g: this.g,
      b: this.b,
      a: this.a
    };
  }
  toRgbString() {
    return this.a !== 1 ? `rgba(${this.r},${this.g},${this.b},${this.a})` : `rgb(${this.r},${this.g},${this.b})`;
  }
  toString() {
    return this.toRgbString();
  }
  // ====================== Privates ======================
  /** Return a new FastColor object with one channel changed */
  _sc(e, r, o) {
    const n = this.clone();
    return n[e] = te(r, o), n;
  }
  _c(e) {
    return new this.constructor(e);
  }
  getMax() {
    return typeof this._max > "u" && (this._max = Math.max(this.r, this.g, this.b)), this._max;
  }
  getMin() {
    return typeof this._min > "u" && (this._min = Math.min(this.r, this.g, this.b)), this._min;
  }
  fromHexString(e) {
    const r = e.replace("#", "");
    function o(n, s) {
      return parseInt(r[n] + r[s || n], 16);
    }
    r.length < 6 ? (this.r = o(0), this.g = o(1), this.b = o(2), this.a = r[3] ? o(3) / 255 : 1) : (this.r = o(0, 1), this.g = o(2, 3), this.b = o(4, 5), this.a = r[6] ? o(6, 7) / 255 : 1);
  }
  fromHsl({
    h: e,
    s: r,
    l: o,
    a: n
  }) {
    if (this._h = e % 360, this._s = r, this._l = o, this.a = typeof n == "number" ? n : 1, r <= 0) {
      const d = $(o * 255);
      this.r = d, this.g = d, this.b = d;
    }
    let s = 0, i = 0, a = 0;
    const l = e / 60, u = (1 - Math.abs(2 * o - 1)) * r, f = u * (1 - Math.abs(l % 2 - 1));
    l >= 0 && l < 1 ? (s = u, i = f) : l >= 1 && l < 2 ? (s = f, i = u) : l >= 2 && l < 3 ? (i = u, a = f) : l >= 3 && l < 4 ? (i = f, a = u) : l >= 4 && l < 5 ? (s = f, a = u) : l >= 5 && l < 6 && (s = u, a = f);
    const c = o - u / 2;
    this.r = $((s + c) * 255), this.g = $((i + c) * 255), this.b = $((a + c) * 255);
  }
  fromHsv({
    h: e,
    s: r,
    v: o,
    a: n
  }) {
    this._h = e % 360, this._s = r, this._v = o, this.a = typeof n == "number" ? n : 1;
    const s = $(o * 255);
    if (this.r = s, this.g = s, this.b = s, r <= 0)
      return;
    const i = e / 60, a = Math.floor(i), l = i - a, u = $(o * (1 - r) * 255), f = $(o * (1 - r * l) * 255), c = $(o * (1 - r * (1 - l)) * 255);
    switch (a) {
      case 0:
        this.g = c, this.b = u;
        break;
      case 1:
        this.r = f, this.b = u;
        break;
      case 2:
        this.r = u, this.b = c;
        break;
      case 3:
        this.r = u, this.g = f;
        break;
      case 4:
        this.r = c, this.g = u;
        break;
      case 5:
      default:
        this.g = u, this.b = f;
        break;
    }
  }
  fromHsvString(e) {
    const r = Ie(e, gt);
    this.fromHsv({
      h: r[0],
      s: r[1],
      v: r[2],
      a: r[3]
    });
  }
  fromHslString(e) {
    const r = Ie(e, gt);
    this.fromHsl({
      h: r[0],
      s: r[1],
      l: r[2],
      a: r[3]
    });
  }
  fromRgbString(e) {
    const r = Ie(e, (o, n) => (
      // Convert percentage to number. e.g. 50% -> 128
      n.includes("%") ? $(o / 100 * 255) : o
    ));
    this.r = r[0], this.g = r[1], this.b = r[2], this.a = r[3];
  }
}
const hr = {
  blue: "#1677FF",
  purple: "#722ED1",
  cyan: "#13C2C2",
  green: "#52C41A",
  magenta: "#EB2F96",
  /**
   * @deprecated Use magenta instead
   */
  pink: "#EB2F96",
  red: "#F5222D",
  orange: "#FA8C16",
  yellow: "#FADB14",
  volcano: "#FA541C",
  geekblue: "#2F54EB",
  gold: "#FAAD14",
  lime: "#A0D911"
}, gr = Object.assign(Object.assign({}, hr), {
  // Color
  colorPrimary: "#1677ff",
  colorSuccess: "#52c41a",
  colorWarning: "#faad14",
  colorError: "#ff4d4f",
  colorInfo: "#1677ff",
  colorLink: "",
  colorTextBase: "",
  colorBgBase: "",
  // Font
  fontFamily: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial,
'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol',
'Noto Color Emoji'`,
  fontFamilyCode: "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace",
  fontSize: 14,
  // Line
  lineWidth: 1,
  lineType: "solid",
  // Motion
  motionUnit: 0.1,
  motionBase: 0,
  motionEaseOutCirc: "cubic-bezier(0.08, 0.82, 0.17, 1)",
  motionEaseInOutCirc: "cubic-bezier(0.78, 0.14, 0.15, 0.86)",
  motionEaseOut: "cubic-bezier(0.215, 0.61, 0.355, 1)",
  motionEaseInOut: "cubic-bezier(0.645, 0.045, 0.355, 1)",
  motionEaseOutBack: "cubic-bezier(0.12, 0.4, 0.29, 1.46)",
  motionEaseInBack: "cubic-bezier(0.71, -0.46, 0.88, 0.6)",
  motionEaseInQuint: "cubic-bezier(0.755, 0.05, 0.855, 0.06)",
  motionEaseOutQuint: "cubic-bezier(0.23, 1, 0.32, 1)",
  // Radius
  borderRadius: 6,
  // Size
  sizeUnit: 4,
  sizeStep: 4,
  sizePopupArrow: 16,
  // Control Base
  controlHeight: 32,
  // zIndex
  zIndexBase: 0,
  zIndexPopupBase: 1e3,
  // Image
  opacityImage: 1,
  // Wireframe
  wireframe: !1,
  // Motion
  motion: !0
});
function Re(t) {
  return t >= 0 && t <= 255;
}
function se(t, e) {
  const {
    r,
    g: o,
    b: n,
    a: s
  } = new N(t).toRgb();
  if (s < 1)
    return t;
  const {
    r: i,
    g: a,
    b: l
  } = new N(e).toRgb();
  for (let u = 0.01; u <= 1; u += 0.01) {
    const f = Math.round((r - i * (1 - u)) / u), c = Math.round((o - a * (1 - u)) / u), d = Math.round((n - l * (1 - u)) / u);
    if (Re(f) && Re(c) && Re(d))
      return new N({
        r: f,
        g: c,
        b: d,
        a: Math.round(u * 100) / 100
      }).toRgbString();
  }
  return new N({
    r,
    g: o,
    b: n,
    a: 1
  }).toRgbString();
}
var pr = function(t, e) {
  var r = {};
  for (var o in t) Object.prototype.hasOwnProperty.call(t, o) && e.indexOf(o) < 0 && (r[o] = t[o]);
  if (t != null && typeof Object.getOwnPropertySymbols == "function") for (var n = 0, o = Object.getOwnPropertySymbols(t); n < o.length; n++)
    e.indexOf(o[n]) < 0 && Object.prototype.propertyIsEnumerable.call(t, o[n]) && (r[o[n]] = t[o[n]]);
  return r;
};
function mr(t) {
  const {
    override: e
  } = t, r = pr(t, ["override"]), o = Object.assign({}, e);
  Object.keys(gr).forEach((d) => {
    delete o[d];
  });
  const n = Object.assign(Object.assign({}, r), o), s = 480, i = 576, a = 768, l = 992, u = 1200, f = 1600;
  if (n.motion === !1) {
    const d = "0s";
    n.motionDurationFast = d, n.motionDurationMid = d, n.motionDurationSlow = d;
  }
  return Object.assign(Object.assign(Object.assign({}, n), {
    // ============== Background ============== //
    colorFillContent: n.colorFillSecondary,
    colorFillContentHover: n.colorFill,
    colorFillAlter: n.colorFillQuaternary,
    colorBgContainerDisabled: n.colorFillTertiary,
    // ============== Split ============== //
    colorBorderBg: n.colorBgContainer,
    colorSplit: se(n.colorBorderSecondary, n.colorBgContainer),
    // ============== Text ============== //
    colorTextPlaceholder: n.colorTextQuaternary,
    colorTextDisabled: n.colorTextQuaternary,
    colorTextHeading: n.colorText,
    colorTextLabel: n.colorTextSecondary,
    colorTextDescription: n.colorTextTertiary,
    colorTextLightSolid: n.colorWhite,
    colorHighlight: n.colorError,
    colorBgTextHover: n.colorFillSecondary,
    colorBgTextActive: n.colorFill,
    colorIcon: n.colorTextTertiary,
    colorIconHover: n.colorText,
    colorErrorOutline: se(n.colorErrorBg, n.colorBgContainer),
    colorWarningOutline: se(n.colorWarningBg, n.colorBgContainer),
    // Font
    fontSizeIcon: n.fontSizeSM,
    // Line
    lineWidthFocus: n.lineWidth * 3,
    // Control
    lineWidth: n.lineWidth,
    controlOutlineWidth: n.lineWidth * 2,
    // Checkbox size and expand icon size
    controlInteractiveSize: n.controlHeight / 2,
    controlItemBgHover: n.colorFillTertiary,
    controlItemBgActive: n.colorPrimaryBg,
    controlItemBgActiveHover: n.colorPrimaryBgHover,
    controlItemBgActiveDisabled: n.colorFill,
    controlTmpOutline: n.colorFillQuaternary,
    controlOutline: se(n.colorPrimaryBg, n.colorBgContainer),
    lineType: n.lineType,
    borderRadius: n.borderRadius,
    borderRadiusXS: n.borderRadiusXS,
    borderRadiusSM: n.borderRadiusSM,
    borderRadiusLG: n.borderRadiusLG,
    fontWeightStrong: 600,
    opacityLoading: 0.65,
    linkDecoration: "none",
    linkHoverDecoration: "none",
    linkFocusDecoration: "none",
    controlPaddingHorizontal: 12,
    controlPaddingHorizontalSM: 8,
    paddingXXS: n.sizeXXS,
    paddingXS: n.sizeXS,
    paddingSM: n.sizeSM,
    padding: n.size,
    paddingMD: n.sizeMD,
    paddingLG: n.sizeLG,
    paddingXL: n.sizeXL,
    paddingContentHorizontalLG: n.sizeLG,
    paddingContentVerticalLG: n.sizeMS,
    paddingContentHorizontal: n.sizeMS,
    paddingContentVertical: n.sizeSM,
    paddingContentHorizontalSM: n.size,
    paddingContentVerticalSM: n.sizeXS,
    marginXXS: n.sizeXXS,
    marginXS: n.sizeXS,
    marginSM: n.sizeSM,
    margin: n.size,
    marginMD: n.sizeMD,
    marginLG: n.sizeLG,
    marginXL: n.sizeXL,
    marginXXL: n.sizeXXL,
    boxShadow: `
      0 6px 16px 0 rgba(0, 0, 0, 0.08),
      0 3px 6px -4px rgba(0, 0, 0, 0.12),
      0 9px 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowSecondary: `
      0 6px 16px 0 rgba(0, 0, 0, 0.08),
      0 3px 6px -4px rgba(0, 0, 0, 0.12),
      0 9px 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowTertiary: `
      0 1px 2px 0 rgba(0, 0, 0, 0.03),
      0 1px 6px -1px rgba(0, 0, 0, 0.02),
      0 2px 4px 0 rgba(0, 0, 0, 0.02)
    `,
    screenXS: s,
    screenXSMin: s,
    screenXSMax: i - 1,
    screenSM: i,
    screenSMMin: i,
    screenSMMax: a - 1,
    screenMD: a,
    screenMDMin: a,
    screenMDMax: l - 1,
    screenLG: l,
    screenLGMin: l,
    screenLGMax: u - 1,
    screenXL: u,
    screenXLMin: u,
    screenXLMax: f - 1,
    screenXXL: f,
    screenXXLMin: f,
    boxShadowPopoverArrow: "2px 2px 5px rgba(0, 0, 0, 0.05)",
    boxShadowCard: `
      0 1px 2px -2px ${new N("rgba(0, 0, 0, 0.16)").toRgbString()},
      0 3px 6px 0 ${new N("rgba(0, 0, 0, 0.12)").toRgbString()},
      0 5px 12px 4px ${new N("rgba(0, 0, 0, 0.09)").toRgbString()}
    `,
    boxShadowDrawerRight: `
      -6px 0 16px 0 rgba(0, 0, 0, 0.08),
      -3px 0 6px -4px rgba(0, 0, 0, 0.12),
      -9px 0 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowDrawerLeft: `
      6px 0 16px 0 rgba(0, 0, 0, 0.08),
      3px 0 6px -4px rgba(0, 0, 0, 0.12),
      9px 0 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowDrawerUp: `
      0 6px 16px 0 rgba(0, 0, 0, 0.08),
      0 3px 6px -4px rgba(0, 0, 0, 0.12),
      0 9px 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowDrawerDown: `
      0 -6px 16px 0 rgba(0, 0, 0, 0.08),
      0 -3px 6px -4px rgba(0, 0, 0, 0.12),
      0 -9px 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowTabsOverflowLeft: "inset 10px 0 8px -8px rgba(0, 0, 0, 0.08)",
    boxShadowTabsOverflowRight: "inset -10px 0 8px -8px rgba(0, 0, 0, 0.08)",
    boxShadowTabsOverflowTop: "inset 0 10px 8px -8px rgba(0, 0, 0, 0.08)",
    boxShadowTabsOverflowBottom: "inset 0 -10px 8px -8px rgba(0, 0, 0, 0.08)"
  }), o);
}
const br = {
  lineHeight: !0,
  lineHeightSM: !0,
  lineHeightLG: !0,
  lineHeightHeading1: !0,
  lineHeightHeading2: !0,
  lineHeightHeading3: !0,
  lineHeightHeading4: !0,
  lineHeightHeading5: !0,
  opacityLoading: !0,
  fontWeightStrong: !0,
  zIndexPopupBase: !0,
  zIndexBase: !0,
  opacityImage: !0
}, yr = {
  size: !0,
  sizeSM: !0,
  sizeLG: !0,
  sizeMD: !0,
  sizeXS: !0,
  sizeXXS: !0,
  sizeMS: !0,
  sizeXL: !0,
  sizeXXL: !0,
  sizeUnit: !0,
  sizeStep: !0,
  motionBase: !0,
  motionUnit: !0
}, vr = Zt($e.defaultAlgorithm), Sr = {
  screenXS: !0,
  screenXSMin: !0,
  screenXSMax: !0,
  screenSM: !0,
  screenSMMin: !0,
  screenSMMax: !0,
  screenMD: !0,
  screenMDMin: !0,
  screenMDMax: !0,
  screenLG: !0,
  screenLGMin: !0,
  screenLGMax: !0,
  screenXL: !0,
  screenXLMin: !0,
  screenXLMax: !0,
  screenXXL: !0,
  screenXXLMin: !0
}, Lt = (t, e, r) => {
  const o = r.getDerivativeToken(t), {
    override: n,
    ...s
  } = e;
  let i = {
    ...o,
    override: n
  };
  return i = mr(i), s && Object.entries(s).forEach(([a, l]) => {
    const {
      theme: u,
      ...f
    } = l;
    let c = f;
    u && (c = Lt({
      ...i,
      ...f
    }, {
      override: f
    }, u)), i[a] = c;
  }), i;
};
function xr() {
  const {
    token: t,
    hashed: e,
    theme: r = vr,
    override: o,
    cssVar: n
  } = g.useContext($e._internalContext), [s, i, a] = en(r, [$e.defaultSeed, t], {
    salt: `${An}-${e || ""}`,
    override: o,
    getComputedToken: Lt,
    cssVar: n && {
      prefix: n.prefix,
      key: n.key,
      unitless: br,
      ignore: yr,
      preserve: Sr
    }
  });
  return [r, a, e ? i : "", s, n];
}
const {
  genStyleHooks: Cr,
  genComponentStyleHook: ro,
  genSubStyleComponent: oo
} = dr({
  usePrefix: () => {
    const {
      getPrefixCls: t,
      iconPrefixCls: e
    } = fe();
    return {
      iconPrefixCls: e,
      rootPrefixCls: t()
    };
  },
  useToken: () => {
    const [t, e, r, o, n] = xr();
    return {
      theme: t,
      realToken: e,
      hashId: r,
      token: o,
      cssVar: n
    };
  },
  useCSP: () => {
    const {
      csp: t
    } = fe();
    return t ?? {};
  },
  layer: {
    name: "antdx",
    dependencies: ["antd"]
  }
});
var wr = `accept acceptCharset accessKey action allowFullScreen allowTransparency
    alt async autoComplete autoFocus autoPlay capture cellPadding cellSpacing challenge
    charSet checked classID className colSpan cols content contentEditable contextMenu
    controls coords crossOrigin data dateTime default defer dir disabled download draggable
    encType form formAction formEncType formMethod formNoValidate formTarget frameBorder
    headers height hidden high href hrefLang htmlFor httpEquiv icon id inputMode integrity
    is keyParams keyType kind label lang list loop low manifest marginHeight marginWidth max maxLength media
    mediaGroup method min minLength multiple muted name noValidate nonce open
    optimum pattern placeholder poster preload radioGroup readOnly rel required
    reversed role rowSpan rows sandbox scope scoped scrolling seamless selected
    shape size sizes span spellCheck src srcDoc srcLang srcSet start step style
    summary tabIndex target title type useMap value width wmode wrap`, _r = `onCopy onCut onPaste onCompositionEnd onCompositionStart onCompositionUpdate onKeyDown
    onKeyPress onKeyUp onFocus onBlur onChange onInput onSubmit onClick onContextMenu onDoubleClick
    onDrag onDragEnd onDragEnter onDragExit onDragLeave onDragOver onDragStart onDrop onMouseDown
    onMouseEnter onMouseLeave onMouseMove onMouseOut onMouseOver onMouseUp onSelect onTouchCancel
    onTouchEnd onTouchMove onTouchStart onScroll onWheel onAbort onCanPlay onCanPlayThrough
    onDurationChange onEmptied onEncrypted onEnded onError onLoadedData onLoadedMetadata
    onLoadStart onPause onPlay onPlaying onProgress onRateChange onSeeked onSeeking onStalled onSuspend onTimeUpdate onVolumeChange onWaiting onLoad onError`, Tr = "".concat(wr, " ").concat(_r).split(/[\s\n]+/), Er = "aria-", Mr = "data-";
function pt(t, e) {
  return t.indexOf(e) === 0;
}
function Or(t) {
  var e = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : !1, r;
  e === !1 ? r = {
    aria: !0,
    data: !0,
    attr: !0
  } : e === !0 ? r = {
    aria: !0
  } : r = D({}, e);
  var o = {};
  return Object.keys(t).forEach(function(n) {
    // Aria
    (r.aria && (n === "role" || pt(n, Er)) || // Data
    r.data && pt(n, Mr) || // Attr
    r.attr && Tr.includes(n)) && (o[n] = t[n]);
  }), o;
}
function ie(t) {
  return typeof t == "string";
}
const Pr = (t, e, r, o) => {
  const [n, s] = I.useState(""), [i, a] = I.useState(1), l = e && ie(t);
  return qn(() => {
    s(t), !l && ie(t) ? a(t.length) : ie(t) && ie(n) && t.indexOf(n) !== 0 && a(1);
  }, [t]), I.useEffect(() => {
    if (l && i < t.length) {
      const f = setTimeout(() => {
        a((c) => c + r);
      }, o);
      return () => {
        clearTimeout(f);
      };
    }
  }, [i, e, t]), [l ? t.slice(0, i) : t, l && i < t.length];
};
function Ir(t) {
  return I.useMemo(() => {
    if (!t)
      return [!1, 0, 0, null];
    let e = {
      step: 1,
      interval: 50,
      // set default suffix is empty
      suffix: null
    };
    return typeof t == "object" && (e = {
      ...e,
      ...t
    }), [!0, e.step, e.interval, e.suffix];
  }, [t]);
}
const Rr = ({
  prefixCls: t
}) => /* @__PURE__ */ g.createElement("span", {
  className: `${t}-dot`
}, /* @__PURE__ */ g.createElement("i", {
  className: `${t}-dot-item`,
  key: "item-1"
}), /* @__PURE__ */ g.createElement("i", {
  className: `${t}-dot-item`,
  key: "item-2"
}), /* @__PURE__ */ g.createElement("i", {
  className: `${t}-dot-item`,
  key: "item-3"
})), kr = (t) => {
  const {
    componentCls: e,
    paddingSM: r,
    padding: o
  } = t;
  return {
    [e]: {
      [`${e}-content`]: {
        // Shared: filled, outlined, shadow
        "&-filled,&-outlined,&-shadow": {
          padding: `${re(r)} ${re(o)}`,
          borderRadius: t.borderRadiusLG
        },
        // Filled:
        "&-filled": {
          backgroundColor: t.colorFillContent
        },
        // Outlined:
        "&-outlined": {
          border: `1px solid ${t.colorBorderSecondary}`
        },
        // Shadow:
        "&-shadow": {
          boxShadow: t.boxShadowTertiary
        }
      }
    }
  };
}, jr = (t) => {
  const {
    componentCls: e,
    fontSize: r,
    lineHeight: o,
    paddingSM: n,
    padding: s,
    calc: i
  } = t, a = i(r).mul(o).div(2).add(n).equal(), l = `${e}-content`;
  return {
    [e]: {
      [l]: {
        // round:
        "&-round": {
          borderRadius: {
            _skip_check_: !0,
            value: a
          },
          paddingInline: i(s).mul(1.25).equal()
        }
      },
      // corner:
      [`&-start ${l}-corner`]: {
        borderStartStartRadius: t.borderRadiusXS
      },
      [`&-end ${l}-corner`]: {
        borderStartEndRadius: t.borderRadiusXS
      }
    }
  };
}, Lr = (t) => {
  const {
    componentCls: e,
    padding: r
  } = t;
  return {
    [`${e}-list`]: {
      display: "flex",
      flexDirection: "column",
      gap: r,
      overflowY: "auto"
    }
  };
}, $r = new yt("loadingMove", {
  "0%": {
    transform: "translateY(0)"
  },
  "10%": {
    transform: "translateY(4px)"
  },
  "20%": {
    transform: "translateY(0)"
  },
  "30%": {
    transform: "translateY(-4px)"
  },
  "40%": {
    transform: "translateY(0)"
  }
}), Dr = new yt("cursorBlink", {
  "0%": {
    opacity: 1
  },
  "50%": {
    opacity: 0
  },
  "100%": {
    opacity: 1
  }
}), Hr = (t) => {
  const {
    componentCls: e,
    fontSize: r,
    lineHeight: o,
    paddingSM: n,
    colorText: s,
    calc: i
  } = t;
  return {
    [e]: {
      display: "flex",
      columnGap: n,
      [`&${e}-end`]: {
        justifyContent: "end",
        flexDirection: "row-reverse",
        [`& ${e}-content-wrapper`]: {
          alignItems: "flex-end"
        }
      },
      [`&${e}-rtl`]: {
        direction: "rtl"
      },
      [`&${e}-typing ${e}-content:last-child::after`]: {
        content: '"|"',
        fontWeight: 900,
        userSelect: "none",
        opacity: 1,
        marginInlineStart: "0.1em",
        animationName: Dr,
        animationDuration: "0.8s",
        animationIterationCount: "infinite",
        animationTimingFunction: "linear"
      },
      // ============================ Avatar =============================
      [`& ${e}-avatar`]: {
        display: "inline-flex",
        justifyContent: "center",
        alignSelf: "flex-start"
      },
      // ======================== Header & Footer ========================
      [`& ${e}-header, & ${e}-footer`]: {
        fontSize: r,
        lineHeight: o,
        color: t.colorText
      },
      [`& ${e}-header`]: {
        marginBottom: t.paddingXXS
      },
      [`& ${e}-footer`]: {
        marginTop: n
      },
      // =========================== Content =============================
      [`& ${e}-content-wrapper`]: {
        flex: "auto",
        display: "flex",
        flexDirection: "column",
        alignItems: "flex-start",
        minWidth: 0,
        maxWidth: "100%"
      },
      [`& ${e}-content`]: {
        position: "relative",
        boxSizing: "border-box",
        minWidth: 0,
        maxWidth: "100%",
        color: s,
        fontSize: t.fontSize,
        lineHeight: t.lineHeight,
        minHeight: i(n).mul(2).add(i(o).mul(r)).equal(),
        wordBreak: "break-word",
        [`& ${e}-dot`]: {
          position: "relative",
          height: "100%",
          display: "flex",
          alignItems: "center",
          columnGap: t.marginXS,
          padding: `0 ${re(t.paddingXXS)}`,
          "&-item": {
            backgroundColor: t.colorPrimary,
            borderRadius: "100%",
            width: 4,
            height: 4,
            animationName: $r,
            animationDuration: "2s",
            animationIterationCount: "infinite",
            animationTimingFunction: "linear",
            "&:nth-child(1)": {
              animationDelay: "0s"
            },
            "&:nth-child(2)": {
              animationDelay: "0.2s"
            },
            "&:nth-child(3)": {
              animationDelay: "0.4s"
            }
          }
        }
      }
    }
  };
}, Br = () => ({}), $t = Cr("Bubble", (t) => {
  const e = Ne(t, {});
  return [Hr(e), Lr(e), kr(e), jr(e)];
}, Br), Dt = /* @__PURE__ */ g.createContext({}), zr = (t, e) => {
  const {
    prefixCls: r,
    className: o,
    rootClassName: n,
    style: s,
    classNames: i = {},
    styles: a = {},
    avatar: l,
    placement: u = "start",
    loading: f = !1,
    loadingRender: c,
    typing: d,
    content: m = "",
    messageRender: v,
    variant: h = "filled",
    shape: b,
    onTypingComplete: y,
    header: E,
    footer: k,
    ...p
  } = t, {
    onUpdate: x
  } = g.useContext(Dt), C = g.useRef(null);
  g.useImperativeHandle(e, () => ({
    nativeElement: C.current
  }));
  const {
    direction: M,
    getPrefixCls: O
  } = fe(), S = O("bubble", r), P = Nn("bubble"), [B, L, z, w] = Ir(d), [_, j] = Pr(m, B, L, z);
  g.useEffect(() => {
    x == null || x();
  }, [_]);
  const A = g.useRef(!1);
  g.useEffect(() => {
    !j && !f ? A.current || (A.current = !0, y == null || y()) : A.current = !1;
  }, [j, f]);
  const [V, W, K] = $t(S), J = Y(S, n, P.className, o, W, K, `${S}-${u}`, {
    [`${S}-rtl`]: M === "rtl",
    [`${S}-typing`]: j && !f && !v && !w
  }), Z = /* @__PURE__ */ g.isValidElement(l) ? l : /* @__PURE__ */ g.createElement(Qt, l), ee = v ? v(_) : _;
  let F;
  f ? F = c ? c() : /* @__PURE__ */ g.createElement(Rr, {
    prefixCls: S
  }) : F = /* @__PURE__ */ g.createElement(g.Fragment, null, ee, j && w);
  let U = /* @__PURE__ */ g.createElement("div", {
    style: {
      ...P.styles.content,
      ...a.content
    },
    className: Y(`${S}-content`, `${S}-content-${h}`, b && `${S}-content-${b}`, P.classNames.content, i.content)
  }, F);
  return (E || k) && (U = /* @__PURE__ */ g.createElement("div", {
    className: `${S}-content-wrapper`
  }, E && /* @__PURE__ */ g.createElement("div", {
    className: Y(`${S}-header`, P.classNames.header, i.header),
    style: {
      ...P.styles.header,
      ...a.header
    }
  }, E), U, k && /* @__PURE__ */ g.createElement("div", {
    className: Y(`${S}-footer`, P.classNames.footer, i.footer),
    style: {
      ...P.styles.footer,
      ...a.footer
    }
  }, k))), V(/* @__PURE__ */ g.createElement("div", oe({
    style: {
      ...P.style,
      ...s
    },
    className: J
  }, p, {
    ref: C
  }), l && /* @__PURE__ */ g.createElement("div", {
    style: {
      ...P.styles.avatar,
      ...a.avatar
    },
    className: Y(`${S}-avatar`, P.classNames.avatar, i.avatar)
  }, Z), U));
}, Ve = /* @__PURE__ */ g.forwardRef(zr);
function Ar(t) {
  const [e, r] = g.useState(t.length), o = g.useMemo(() => t.slice(0, e), [t, e]), n = g.useMemo(() => {
    const i = o[o.length - 1];
    return i ? i.key : null;
  }, [o]);
  g.useEffect(() => {
    var i;
    if (!(o.length && o.every((a, l) => {
      var u;
      return a.key === ((u = t[l]) == null ? void 0 : u.key);
    }))) {
      if (o.length === 0)
        r(1);
      else
        for (let a = 0; a < o.length; a += 1)
          if (o[a].key !== ((i = t[a]) == null ? void 0 : i.key)) {
            r(a);
            break;
          }
    }
  }, [t]);
  const s = Tt((i) => {
    i === n && r(e + 1);
  });
  return [o, s];
}
function Fr(t, e) {
  const r = I.useCallback((o) => typeof e == "function" ? e(o) : e ? e[o.role] || {} : {}, [e]);
  return I.useMemo(() => (t || []).map((o, n) => {
    const s = o.key ?? `preset_${n}`;
    return {
      ...r(o),
      ...o,
      key: s
    };
  }), [t, r]);
}
const Xr = 1, Nr = (t, e) => {
  const {
    prefixCls: r,
    rootClassName: o,
    className: n,
    items: s,
    autoScroll: i = !0,
    roles: a,
    ...l
  } = t, u = Or(l, {
    attr: !0,
    aria: !0
  }), f = I.useRef(null), c = I.useRef({}), {
    getPrefixCls: d
  } = fe(), m = d("bubble", r), v = `${m}-list`, [h, b, y] = $t(m), [E, k] = I.useState(!1);
  I.useEffect(() => (k(!0), () => {
    k(!1);
  }), []);
  const p = Fr(s, a), [x, C] = Ar(p), [M, O] = I.useState(!0), [S, P] = I.useState(0), B = (w) => {
    const _ = w.target;
    O(_.scrollHeight - Math.abs(_.scrollTop) - _.clientHeight <= Xr);
  };
  I.useEffect(() => {
    i && f.current && M && f.current.scrollTo({
      top: f.current.scrollHeight
    });
  }, [S]), I.useEffect(() => {
    var w;
    if (i) {
      const _ = (w = x[x.length - 2]) == null ? void 0 : w.key, j = c.current[_];
      if (j) {
        const {
          nativeElement: A
        } = j, {
          top: V,
          bottom: W
        } = A.getBoundingClientRect(), {
          top: K,
          bottom: J
        } = f.current.getBoundingClientRect();
        V < J && W > K && (P((ee) => ee + 1), O(!0));
      }
    }
  }, [x.length]), I.useImperativeHandle(e, () => ({
    nativeElement: f.current,
    scrollTo: ({
      key: w,
      offset: _,
      behavior: j = "smooth",
      block: A
    }) => {
      if (typeof _ == "number")
        f.current.scrollTo({
          top: _,
          behavior: j
        });
      else if (w !== void 0) {
        const V = c.current[w];
        if (V) {
          const W = x.findIndex((K) => K.key === w);
          O(W === x.length - 1), V.nativeElement.scrollIntoView({
            behavior: j,
            block: A
          });
        }
      }
    }
  }));
  const L = Tt(() => {
    i && P((w) => w + 1);
  }), z = I.useMemo(() => ({
    onUpdate: L
  }), []);
  return h(/* @__PURE__ */ I.createElement(Dt.Provider, {
    value: z
  }, /* @__PURE__ */ I.createElement("div", oe({}, u, {
    className: Y(v, o, n, b, y, {
      [`${v}-reach-end`]: M
    }),
    ref: f,
    onScroll: B
  }), x.map(({
    key: w,
    ..._
  }) => /* @__PURE__ */ I.createElement(Ve, oe({}, _, {
    key: w,
    ref: (j) => {
      j ? c.current[w] = j : delete c.current[w];
    },
    typing: E ? _.typing : !1,
    onTypingComplete: () => {
      var j;
      (j = _.onTypingComplete) == null || j.call(_), C(w);
    }
  }))))));
}, Vr = /* @__PURE__ */ I.forwardRef(Nr);
Ve.List = Vr;
function Wr(t) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(t.trim());
}
function Ur(t, e = !1) {
  try {
    if (Kt(t))
      return t;
    if (e && !Wr(t))
      return;
    if (typeof t == "string") {
      let r = t.trim();
      return r.startsWith(";") && (r = r.slice(1)), r.endsWith(";") && (r = r.slice(0, -1)), new Function(`return (...args) => (${r})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function Gr(t, e) {
  return ke(() => Ur(t, e), [t, e]);
}
const Kr = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function qr(t) {
  return t ? Object.keys(t).reduce((e, r) => {
    const o = t[r];
    return e[r] = Yr(r, o), e;
  }, {}) : {};
}
function Yr(t, e) {
  return typeof e == "number" && !Kr.includes(t) ? e + "px" : e;
}
function ze(t) {
  const e = [], r = t.cloneNode(!1);
  if (t._reactElement) {
    const n = g.Children.toArray(t._reactElement.props.children).map((s) => {
      if (g.isValidElement(s) && s.props.__slot__) {
        const {
          portals: i,
          clonedElement: a
        } = ze(s.props.el);
        return g.cloneElement(s, {
          ...s.props,
          el: a,
          children: [...g.Children.toArray(s.props.children), ...i]
        });
      }
      return null;
    });
    return n.originalChildren = t._reactElement.props.children, e.push(je(g.cloneElement(t._reactElement, {
      ...t._reactElement.props,
      children: n
    }), r)), {
      clonedElement: r,
      portals: e
    };
  }
  Object.keys(t.getEventListeners()).forEach((n) => {
    t.getEventListeners(n).forEach(({
      listener: i,
      type: a,
      useCapture: l
    }) => {
      r.addEventListener(a, i, l);
    });
  });
  const o = Array.from(t.childNodes);
  for (let n = 0; n < o.length; n++) {
    const s = o[n];
    if (s.nodeType === 1) {
      const {
        clonedElement: i,
        portals: a
      } = ze(s);
      e.push(...a), r.appendChild(i);
    } else s.nodeType === 3 && r.appendChild(s.cloneNode());
  }
  return {
    clonedElement: r,
    portals: e
  };
}
function Qr(t, e) {
  t && (typeof t == "function" ? t(e) : t.current = e);
}
const mt = Ft(({
  slot: t,
  clone: e,
  className: r,
  style: o,
  observeAttributes: n
}, s) => {
  const i = Xt(), [a, l] = Nt([]), {
    forceClone: u
  } = qt(), f = u ? !0 : e;
  return Vt(() => {
    var v;
    if (!i.current || !t)
      return;
    let c = t;
    function d() {
      let h = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (h = c.children[0], h.tagName.toLowerCase() === "react-portal-target" && h.children[0] && (h = h.children[0])), Qr(s, h), r && h.classList.add(...r.split(" ")), o) {
        const b = qr(o);
        Object.keys(b).forEach((y) => {
          h.style[y] = b[y];
        });
      }
    }
    let m = null;
    if (f && window.MutationObserver) {
      let h = function() {
        var k, p, x;
        (k = i.current) != null && k.contains(c) && ((p = i.current) == null || p.removeChild(c));
        const {
          portals: y,
          clonedElement: E
        } = ze(t);
        c = E, l(y), c.style.display = "contents", d(), (x = i.current) == null || x.appendChild(c);
      };
      h();
      const b = hn(() => {
        h(), m == null || m.disconnect(), m == null || m.observe(t, {
          childList: !0,
          subtree: !0,
          attributes: n
        });
      }, 50);
      m = new window.MutationObserver(b), m.observe(t, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", d(), (v = i.current) == null || v.appendChild(c);
    return () => {
      var h, b;
      c.style.display = "", (h = i.current) != null && h.contains(c) && ((b = i.current) == null || b.removeChild(c)), m == null || m.disconnect();
    };
  }, [t, f, r, o, s, n]), g.createElement("react-child", {
    ref: i,
    style: {
      display: "contents"
    }
  }, ...a);
});
function Ae(t, e, r) {
  const o = t.filter(Boolean);
  if (o.length !== 0)
    return o.map((n, s) => {
      var u;
      if (typeof n != "object")
        return e != null && e.fallback ? e.fallback(n) : n;
      const i = {
        ...n.props,
        key: ((u = n.props) == null ? void 0 : u.key) ?? (r ? `${r}-${s}` : `${s}`)
      };
      let a = i;
      Object.keys(n.slots).forEach((f) => {
        if (!n.slots[f] || !(n.slots[f] instanceof Element) && !n.slots[f].el)
          return;
        const c = f.split(".");
        c.forEach((y, E) => {
          a[y] || (a[y] = {}), E !== c.length - 1 && (a = i[y]);
        });
        const d = n.slots[f];
        let m, v, h = (e == null ? void 0 : e.clone) ?? !1, b = e == null ? void 0 : e.forceClone;
        d instanceof Element ? m = d : (m = d.el, v = d.callback, h = d.clone ?? h, b = d.forceClone ?? b), b = b ?? !!v, a[c[c.length - 1]] = m ? v ? (...y) => (v(c[c.length - 1], y), /* @__PURE__ */ G.jsx(Ke, {
          params: y,
          forceClone: b,
          children: /* @__PURE__ */ G.jsx(mt, {
            slot: m,
            clone: h
          })
        })) : /* @__PURE__ */ G.jsx(Ke, {
          forceClone: b,
          children: /* @__PURE__ */ G.jsx(mt, {
            slot: m,
            clone: h
          })
        }) : a[c[c.length - 1]], a = i;
      });
      const l = (e == null ? void 0 : e.children) || "children";
      return n[l] ? i[l] = Ae(n[l], e, `${s}`) : e != null && e.children && (i[l] = void 0, Reflect.deleteProperty(i, l)), i;
    });
}
const {
  useItems: Jr,
  withItemsContextProvider: Zr,
  ItemHandler: so
} = bt("antdx-bubble.list-items"), {
  useItems: eo,
  withItemsContextProvider: to,
  ItemHandler: io
} = bt("antdx-bubble.list-roles"), ao = zn(to(["roles"], Zr(["items", "default"], ({
  items: t,
  roles: e,
  children: r,
  ...o
}) => {
  const n = Gr(e), {
    items: {
      roles: s
    }
  } = eo(), {
    items: i
  } = Jr(), a = ke(() => {
    var u;
    return e || ((u = Ae(s, {
      clone: !0,
      forceClone: !0
    })) == null ? void 0 : u.reduce((f, c) => (c.role !== void 0 && (f[c.role] = c), f), {}));
  }, [s, e]), l = i.items.length > 0 ? i.items : i.default;
  return /* @__PURE__ */ G.jsxs(G.Fragment, {
    children: [/* @__PURE__ */ G.jsx("div", {
      style: {
        display: "none"
      },
      children: r
    }), /* @__PURE__ */ G.jsx(Ve.List, {
      ...o,
      items: ke(() => t || Ae(l), [t, l]),
      roles: n || a
    })]
  });
})));
export {
  ao as BubbleList,
  ao as default
};
