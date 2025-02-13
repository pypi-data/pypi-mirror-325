import { i as Qt, a as et, r as Xt, g as Vt, w as M, b as $t } from "./Index-BLfZgKfr.js";
const x = window.ms_globals.React, qt = window.ms_globals.React.forwardRef, Yt = window.ms_globals.React.useRef, zt = window.ms_globals.React.useState, Tt = window.ms_globals.React.useEffect, Jt = window.ms_globals.React.useMemo, tt = window.ms_globals.ReactDOM.createPortal, te = window.ms_globals.internalContext.useContextPropsContext, mt = window.ms_globals.internalContext.ContextPropsProvider, ee = window.ms_globals.antdCssinjs.StyleProvider, ht = window.ms_globals.antd.theme, ne = window.ms_globals.antd.ConfigProvider, re = window.ms_globals.dayjs;
var ie = /\s/;
function ae(e) {
  for (var t = e.length; t-- && ie.test(e.charAt(t)); )
    ;
  return t;
}
var oe = /^\s+/;
function se(e) {
  return e && e.slice(0, ae(e) + 1).replace(oe, "");
}
var pt = NaN, le = /^[-+]0x[0-9a-f]+$/i, ce = /^0b[01]+$/i, ue = /^0o[0-7]+$/i, de = parseInt;
function yt(e) {
  if (typeof e == "number")
    return e;
  if (Qt(e))
    return pt;
  if (et(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = et(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = se(e);
  var n = ce.test(e);
  return n || ue.test(e) ? de(e.slice(2), n ? 2 : 8) : le.test(e) ? pt : +e;
}
var J = function() {
  return Xt.Date.now();
}, fe = "Expected a function", me = Math.max, he = Math.min;
function pe(e, t, n) {
  var r, i, a, o, s, l, h = 0, p = !1, c = !1, _ = !0;
  if (typeof e != "function")
    throw new TypeError(fe);
  t = yt(t) || 0, et(n) && (p = !!n.leading, c = "maxWait" in n, a = c ? me(yt(n.maxWait) || 0, t) : a, _ = "trailing" in n ? !!n.trailing : _);
  function m(f) {
    var C = r, F = i;
    return r = i = void 0, h = f, o = e.apply(F, C), o;
  }
  function k(f) {
    return h = f, s = setTimeout(w, t), p ? m(f) : o;
  }
  function d(f) {
    var C = f - l, F = f - h, ft = t - C;
    return c ? he(ft, a - F) : ft;
  }
  function y(f) {
    var C = f - l, F = f - h;
    return l === void 0 || C >= t || C < 0 || c && F >= a;
  }
  function w() {
    var f = J();
    if (y(f))
      return E(f);
    s = setTimeout(w, d(f));
  }
  function E(f) {
    return s = void 0, _ && r ? m(f) : (r = i = void 0, o);
  }
  function v() {
    s !== void 0 && clearTimeout(s), h = 0, r = l = i = s = void 0;
  }
  function u() {
    return s === void 0 ? o : E(J());
  }
  function b() {
    var f = J(), C = y(f);
    if (r = arguments, i = this, l = f, C) {
      if (s === void 0)
        return k(l);
      if (c)
        return clearTimeout(s), s = setTimeout(w, t), m(l);
    }
    return s === void 0 && (s = setTimeout(w, t)), o;
  }
  return b.cancel = v, b.flush = u, b;
}
var At = {
  exports: {}
}, G = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var ye = x, _e = Symbol.for("react.element"), we = Symbol.for("react.fragment"), Pe = Object.prototype.hasOwnProperty, ge = ye.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, be = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Ft(e, t, n) {
  var r, i = {}, a = null, o = null;
  n !== void 0 && (a = "" + n), t.key !== void 0 && (a = "" + t.key), t.ref !== void 0 && (o = t.ref);
  for (r in t) Pe.call(t, r) && !be.hasOwnProperty(r) && (i[r] = t[r]);
  if (e && e.defaultProps) for (r in t = e.defaultProps, t) i[r] === void 0 && (i[r] = t[r]);
  return {
    $$typeof: _e,
    type: e,
    key: a,
    ref: o,
    props: i,
    _owner: ge.current
  };
}
G.Fragment = we;
G.jsx = Ft;
G.jsxs = Ft;
At.exports = G;
var I = At.exports;
const {
  SvelteComponent: je,
  assign: _t,
  binding_callbacks: wt,
  check_outros: ke,
  children: Nt,
  claim_element: Dt,
  claim_space: Ee,
  component_subscribe: Pt,
  compute_slots: ve,
  create_slot: Ce,
  detach: z,
  element: Mt,
  empty: gt,
  exclude_internal_props: bt,
  get_all_dirty_from_scope: Se,
  get_slot_changes: xe,
  group_outros: Ie,
  init: Oe,
  insert_hydration: L,
  safe_not_equal: Re,
  set_custom_element_data: Lt,
  space: ze,
  transition_in: W,
  transition_out: nt,
  update_slot_base: Te
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ae,
  getContext: Fe,
  onDestroy: Ne,
  setContext: De
} = window.__gradio__svelte__internal;
function jt(e) {
  let t, n;
  const r = (
    /*#slots*/
    e[7].default
  ), i = Ce(
    r,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = Mt("svelte-slot"), i && i.c(), this.h();
    },
    l(a) {
      t = Dt(a, "SVELTE-SLOT", {
        class: !0
      });
      var o = Nt(t);
      i && i.l(o), o.forEach(z), this.h();
    },
    h() {
      Lt(t, "class", "svelte-1rt0kpf");
    },
    m(a, o) {
      L(a, t, o), i && i.m(t, null), e[9](t), n = !0;
    },
    p(a, o) {
      i && i.p && (!n || o & /*$$scope*/
      64) && Te(
        i,
        r,
        a,
        /*$$scope*/
        a[6],
        n ? xe(
          r,
          /*$$scope*/
          a[6],
          o,
          null
        ) : Se(
          /*$$scope*/
          a[6]
        ),
        null
      );
    },
    i(a) {
      n || (W(i, a), n = !0);
    },
    o(a) {
      nt(i, a), n = !1;
    },
    d(a) {
      a && z(t), i && i.d(a), e[9](null);
    }
  };
}
function Me(e) {
  let t, n, r, i, a = (
    /*$$slots*/
    e[4].default && jt(e)
  );
  return {
    c() {
      t = Mt("react-portal-target"), n = ze(), a && a.c(), r = gt(), this.h();
    },
    l(o) {
      t = Dt(o, "REACT-PORTAL-TARGET", {
        class: !0
      }), Nt(t).forEach(z), n = Ee(o), a && a.l(o), r = gt(), this.h();
    },
    h() {
      Lt(t, "class", "svelte-1rt0kpf");
    },
    m(o, s) {
      L(o, t, s), e[8](t), L(o, n, s), a && a.m(o, s), L(o, r, s), i = !0;
    },
    p(o, [s]) {
      /*$$slots*/
      o[4].default ? a ? (a.p(o, s), s & /*$$slots*/
      16 && W(a, 1)) : (a = jt(o), a.c(), W(a, 1), a.m(r.parentNode, r)) : a && (Ie(), nt(a, 1, 1, () => {
        a = null;
      }), ke());
    },
    i(o) {
      i || (W(a), i = !0);
    },
    o(o) {
      nt(a), i = !1;
    },
    d(o) {
      o && (z(t), z(n), z(r)), e[8](null), a && a.d(o);
    }
  };
}
function kt(e) {
  const {
    svelteInit: t,
    ...n
  } = e;
  return n;
}
function Le(e, t, n) {
  let r, i, {
    $$slots: a = {},
    $$scope: o
  } = t;
  const s = ve(a);
  let {
    svelteInit: l
  } = t;
  const h = M(kt(t)), p = M();
  Pt(e, p, (u) => n(0, r = u));
  const c = M();
  Pt(e, c, (u) => n(1, i = u));
  const _ = [], m = Fe("$$ms-gr-react-wrapper"), {
    slotKey: k,
    slotIndex: d,
    subSlotIndex: y
  } = Vt() || {}, w = l({
    parent: m,
    props: h,
    target: p,
    slot: c,
    slotKey: k,
    slotIndex: d,
    subSlotIndex: y,
    onDestroy(u) {
      _.push(u);
    }
  });
  De("$$ms-gr-react-wrapper", w), Ae(() => {
    h.set(kt(t));
  }), Ne(() => {
    _.forEach((u) => u());
  });
  function E(u) {
    wt[u ? "unshift" : "push"](() => {
      r = u, p.set(r);
    });
  }
  function v(u) {
    wt[u ? "unshift" : "push"](() => {
      i = u, c.set(i);
    });
  }
  return e.$$set = (u) => {
    n(17, t = _t(_t({}, t), bt(u))), "svelteInit" in u && n(5, l = u.svelteInit), "$$scope" in u && n(6, o = u.$$scope);
  }, t = bt(t), [r, i, p, c, s, l, o, a, E, v];
}
class We extends je {
  constructor(t) {
    super(), Oe(this, t, Le, Me, Re, {
      svelteInit: 5
    });
  }
}
const Et = window.ms_globals.rerender, Q = window.ms_globals.tree;
function Ke(e, t = {}) {
  function n(r) {
    const i = M(), a = new We({
      ...r,
      props: {
        svelteInit(o) {
          window.ms_globals.autokey += 1;
          const s = {
            key: window.ms_globals.autokey,
            svelteInstance: i,
            reactComponent: e,
            props: o.props,
            slot: o.slot,
            target: o.target,
            slotIndex: o.slotIndex,
            subSlotIndex: o.subSlotIndex,
            ignore: t.ignore,
            slotKey: o.slotKey,
            nodes: []
          }, l = o.parent ?? Q;
          return l.nodes = [...l.nodes, s], Et({
            createPortal: tt,
            node: Q
          }), o.onDestroy(() => {
            l.nodes = l.nodes.filter((h) => h.svelteInstance !== i), Et({
              createPortal: tt,
              node: Q
            });
          }), s;
        },
        ...r.props
      }
    });
    return i.set(a), a;
  }
  return new Promise((r) => {
    window.ms_globals.initializePromise.then(() => {
      r(n);
    });
  });
}
const Ue = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Be(e) {
  return e ? Object.keys(e).reduce((t, n) => {
    const r = e[n];
    return t[n] = Ge(n, r), t;
  }, {}) : {};
}
function Ge(e, t) {
  return typeof t == "number" && !Ue.includes(e) ? t + "px" : t;
}
function rt(e) {
  const t = [], n = e.cloneNode(!1);
  if (e._reactElement) {
    const i = x.Children.toArray(e._reactElement.props.children).map((a) => {
      if (x.isValidElement(a) && a.props.__slot__) {
        const {
          portals: o,
          clonedElement: s
        } = rt(a.props.el);
        return x.cloneElement(a, {
          ...a.props,
          el: s,
          children: [...x.Children.toArray(a.props.children), ...o]
        });
      }
      return null;
    });
    return i.originalChildren = e._reactElement.props.children, t.push(tt(x.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: i
    }), n)), {
      clonedElement: n,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((i) => {
    e.getEventListeners(i).forEach(({
      listener: o,
      type: s,
      useCapture: l
    }) => {
      n.addEventListener(s, o, l);
    });
  });
  const r = Array.from(e.childNodes);
  for (let i = 0; i < r.length; i++) {
    const a = r[i];
    if (a.nodeType === 1) {
      const {
        clonedElement: o,
        portals: s
      } = rt(a);
      t.push(...s), n.appendChild(o);
    } else a.nodeType === 3 && n.appendChild(a.cloneNode());
  }
  return {
    clonedElement: n,
    portals: t
  };
}
function He(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const Wt = qt(({
  slot: e,
  clone: t,
  className: n,
  style: r,
  observeAttributes: i
}, a) => {
  const o = Yt(), [s, l] = zt([]), {
    forceClone: h
  } = te(), p = h ? !0 : t;
  return Tt(() => {
    var k;
    if (!o.current || !e)
      return;
    let c = e;
    function _() {
      let d = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (d = c.children[0], d.tagName.toLowerCase() === "react-portal-target" && d.children[0] && (d = d.children[0])), He(a, d), n && d.classList.add(...n.split(" ")), r) {
        const y = Be(r);
        Object.keys(y).forEach((w) => {
          d.style[w] = y[w];
        });
      }
    }
    let m = null;
    if (p && window.MutationObserver) {
      let d = function() {
        var v, u, b;
        (v = o.current) != null && v.contains(c) && ((u = o.current) == null || u.removeChild(c));
        const {
          portals: w,
          clonedElement: E
        } = rt(e);
        c = E, l(w), c.style.display = "contents", _(), (b = o.current) == null || b.appendChild(c);
      };
      d();
      const y = pe(() => {
        d(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      m = new window.MutationObserver(y), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", _(), (k = o.current) == null || k.appendChild(c);
    return () => {
      var d, y;
      c.style.display = "", (d = o.current) != null && d.contains(c) && ((y = o.current) == null || y.removeChild(c)), m == null || m.disconnect();
    };
  }, [e, p, n, r, a, i]), x.createElement("react-child", {
    ref: o,
    style: {
      display: "contents"
    }
  }, ...s);
});
function Ze(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function qe(e, t = !1) {
  try {
    if ($t(e))
      return e;
    if (t && !Ze(e))
      return;
    if (typeof e == "string") {
      let n = e.trim();
      return n.startsWith(";") && (n = n.slice(1)), n.endsWith(";") && (n = n.slice(0, -1)), new Function(`return (...args) => (${n})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function X(e, t) {
  return Jt(() => qe(e, t), [e, t]);
}
function vt(e, t) {
  return e ? /* @__PURE__ */ I.jsx(Wt, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function Ye({
  key: e,
  slots: t,
  targets: n
}, r) {
  return t[e] ? (...i) => n ? n.map((a, o) => /* @__PURE__ */ I.jsx(mt, {
    params: i,
    forceClone: !0,
    children: vt(a, {
      clone: !0,
      ...r
    })
  }, o)) : /* @__PURE__ */ I.jsx(mt, {
    params: i,
    forceClone: !0,
    children: vt(t[e], {
      clone: !0,
      ...r
    })
  }) : void 0;
}
var Kt = Symbol.for("immer-nothing"), Ct = Symbol.for("immer-draftable"), P = Symbol.for("immer-state");
function j(e, ...t) {
  throw new Error(`[Immer] minified error nr: ${e}. Full error at: https://bit.ly/3cXEKWf`);
}
var T = Object.getPrototypeOf;
function A(e) {
  return !!e && !!e[P];
}
function O(e) {
  var t;
  return e ? Ut(e) || Array.isArray(e) || !!e[Ct] || !!((t = e.constructor) != null && t[Ct]) || Z(e) || q(e) : !1;
}
var Je = Object.prototype.constructor.toString();
function Ut(e) {
  if (!e || typeof e != "object") return !1;
  const t = T(e);
  if (t === null)
    return !0;
  const n = Object.hasOwnProperty.call(t, "constructor") && t.constructor;
  return n === Object ? !0 : typeof n == "function" && Function.toString.call(n) === Je;
}
function K(e, t) {
  H(e) === 0 ? Reflect.ownKeys(e).forEach((n) => {
    t(n, e[n], e);
  }) : e.forEach((n, r) => t(r, n, e));
}
function H(e) {
  const t = e[P];
  return t ? t.type_ : Array.isArray(e) ? 1 : Z(e) ? 2 : q(e) ? 3 : 0;
}
function it(e, t) {
  return H(e) === 2 ? e.has(t) : Object.prototype.hasOwnProperty.call(e, t);
}
function Bt(e, t, n) {
  const r = H(e);
  r === 2 ? e.set(t, n) : r === 3 ? e.add(n) : e[t] = n;
}
function Qe(e, t) {
  return e === t ? e !== 0 || 1 / e === 1 / t : e !== e && t !== t;
}
function Z(e) {
  return e instanceof Map;
}
function q(e) {
  return e instanceof Set;
}
function S(e) {
  return e.copy_ || e.base_;
}
function at(e, t) {
  if (Z(e))
    return new Map(e);
  if (q(e))
    return new Set(e);
  if (Array.isArray(e)) return Array.prototype.slice.call(e);
  const n = Ut(e);
  if (t === !0 || t === "class_only" && !n) {
    const r = Object.getOwnPropertyDescriptors(e);
    delete r[P];
    let i = Reflect.ownKeys(r);
    for (let a = 0; a < i.length; a++) {
      const o = i[a], s = r[o];
      s.writable === !1 && (s.writable = !0, s.configurable = !0), (s.get || s.set) && (r[o] = {
        configurable: !0,
        writable: !0,
        // could live with !!desc.set as well here...
        enumerable: s.enumerable,
        value: e[o]
      });
    }
    return Object.create(T(e), r);
  } else {
    const r = T(e);
    if (r !== null && n)
      return {
        ...e
      };
    const i = Object.create(r);
    return Object.assign(i, e);
  }
}
function ut(e, t = !1) {
  return Y(e) || A(e) || !O(e) || (H(e) > 1 && (e.set = e.add = e.clear = e.delete = Xe), Object.freeze(e), t && Object.entries(e).forEach(([n, r]) => ut(r, !0))), e;
}
function Xe() {
  j(2);
}
function Y(e) {
  return Object.isFrozen(e);
}
var Ve = {};
function R(e) {
  const t = Ve[e];
  return t || j(0, e), t;
}
var N;
function Gt() {
  return N;
}
function $e(e, t) {
  return {
    drafts_: [],
    parent_: e,
    immer_: t,
    // Whenever the modified draft contains a draft from another scope, we
    // need to prevent auto-freezing so the unowned draft can be finalized.
    canAutoFreeze_: !0,
    unfinalizedDrafts_: 0
  };
}
function St(e, t) {
  t && (R("Patches"), e.patches_ = [], e.inversePatches_ = [], e.patchListener_ = t);
}
function ot(e) {
  st(e), e.drafts_.forEach(tn), e.drafts_ = null;
}
function st(e) {
  e === N && (N = e.parent_);
}
function xt(e) {
  return N = $e(N, e);
}
function tn(e) {
  const t = e[P];
  t.type_ === 0 || t.type_ === 1 ? t.revoke_() : t.revoked_ = !0;
}
function It(e, t) {
  t.unfinalizedDrafts_ = t.drafts_.length;
  const n = t.drafts_[0];
  return e !== void 0 && e !== n ? (n[P].modified_ && (ot(t), j(4)), O(e) && (e = U(t, e), t.parent_ || B(t, e)), t.patches_ && R("Patches").generateReplacementPatches_(n[P].base_, e, t.patches_, t.inversePatches_)) : e = U(t, n, []), ot(t), t.patches_ && t.patchListener_(t.patches_, t.inversePatches_), e !== Kt ? e : void 0;
}
function U(e, t, n) {
  if (Y(t)) return t;
  const r = t[P];
  if (!r)
    return K(t, (i, a) => Ot(e, r, t, i, a, n)), t;
  if (r.scope_ !== e) return t;
  if (!r.modified_)
    return B(e, r.base_, !0), r.base_;
  if (!r.finalized_) {
    r.finalized_ = !0, r.scope_.unfinalizedDrafts_--;
    const i = r.copy_;
    let a = i, o = !1;
    r.type_ === 3 && (a = new Set(i), i.clear(), o = !0), K(a, (s, l) => Ot(e, r, i, s, l, n, o)), B(e, i, !1), n && e.patches_ && R("Patches").generatePatches_(r, n, e.patches_, e.inversePatches_);
  }
  return r.copy_;
}
function Ot(e, t, n, r, i, a, o) {
  if (A(i)) {
    const s = a && t && t.type_ !== 3 && // Set objects are atomic since they have no keys.
    !it(t.assigned_, r) ? a.concat(r) : void 0, l = U(e, i, s);
    if (Bt(n, r, l), A(l))
      e.canAutoFreeze_ = !1;
    else return;
  } else o && n.add(i);
  if (O(i) && !Y(i)) {
    if (!e.immer_.autoFreeze_ && e.unfinalizedDrafts_ < 1)
      return;
    U(e, i), (!t || !t.scope_.parent_) && typeof r != "symbol" && Object.prototype.propertyIsEnumerable.call(n, r) && B(e, i);
  }
}
function B(e, t, n = !1) {
  !e.parent_ && e.immer_.autoFreeze_ && e.canAutoFreeze_ && ut(t, n);
}
function en(e, t) {
  const n = Array.isArray(e), r = {
    type_: n ? 1 : 0,
    // Track which produce call this is associated with.
    scope_: t ? t.scope_ : Gt(),
    // True for both shallow and deep changes.
    modified_: !1,
    // Used during finalization.
    finalized_: !1,
    // Track which properties have been assigned (true) or deleted (false).
    assigned_: {},
    // The parent draft state.
    parent_: t,
    // The base state.
    base_: e,
    // The base proxy.
    draft_: null,
    // set below
    // The base copy with any updated values.
    copy_: null,
    // Called by the `produce` function.
    revoke_: null,
    isManual_: !1
  };
  let i = r, a = dt;
  n && (i = [r], a = D);
  const {
    revoke: o,
    proxy: s
  } = Proxy.revocable(i, a);
  return r.draft_ = s, r.revoke_ = o, s;
}
var dt = {
  get(e, t) {
    if (t === P) return e;
    const n = S(e);
    if (!it(n, t))
      return nn(e, n, t);
    const r = n[t];
    return e.finalized_ || !O(r) ? r : r === V(e.base_, t) ? ($(e), e.copy_[t] = ct(r, e)) : r;
  },
  has(e, t) {
    return t in S(e);
  },
  ownKeys(e) {
    return Reflect.ownKeys(S(e));
  },
  set(e, t, n) {
    const r = Ht(S(e), t);
    if (r != null && r.set)
      return r.set.call(e.draft_, n), !0;
    if (!e.modified_) {
      const i = V(S(e), t), a = i == null ? void 0 : i[P];
      if (a && a.base_ === n)
        return e.copy_[t] = n, e.assigned_[t] = !1, !0;
      if (Qe(n, i) && (n !== void 0 || it(e.base_, t))) return !0;
      $(e), lt(e);
    }
    return e.copy_[t] === n && // special case: handle new props with value 'undefined'
    (n !== void 0 || t in e.copy_) || // special case: NaN
    Number.isNaN(n) && Number.isNaN(e.copy_[t]) || (e.copy_[t] = n, e.assigned_[t] = !0), !0;
  },
  deleteProperty(e, t) {
    return V(e.base_, t) !== void 0 || t in e.base_ ? (e.assigned_[t] = !1, $(e), lt(e)) : delete e.assigned_[t], e.copy_ && delete e.copy_[t], !0;
  },
  // Note: We never coerce `desc.value` into an Immer draft, because we can't make
  // the same guarantee in ES5 mode.
  getOwnPropertyDescriptor(e, t) {
    const n = S(e), r = Reflect.getOwnPropertyDescriptor(n, t);
    return r && {
      writable: !0,
      configurable: e.type_ !== 1 || t !== "length",
      enumerable: r.enumerable,
      value: n[t]
    };
  },
  defineProperty() {
    j(11);
  },
  getPrototypeOf(e) {
    return T(e.base_);
  },
  setPrototypeOf() {
    j(12);
  }
}, D = {};
K(dt, (e, t) => {
  D[e] = function() {
    return arguments[0] = arguments[0][0], t.apply(this, arguments);
  };
});
D.deleteProperty = function(e, t) {
  return D.set.call(this, e, t, void 0);
};
D.set = function(e, t, n) {
  return dt.set.call(this, e[0], t, n, e[0]);
};
function V(e, t) {
  const n = e[P];
  return (n ? S(n) : e)[t];
}
function nn(e, t, n) {
  var i;
  const r = Ht(t, n);
  return r ? "value" in r ? r.value : (
    // This is a very special case, if the prop is a getter defined by the
    // prototype, we should invoke it with the draft as context!
    (i = r.get) == null ? void 0 : i.call(e.draft_)
  ) : void 0;
}
function Ht(e, t) {
  if (!(t in e)) return;
  let n = T(e);
  for (; n; ) {
    const r = Object.getOwnPropertyDescriptor(n, t);
    if (r) return r;
    n = T(n);
  }
}
function lt(e) {
  e.modified_ || (e.modified_ = !0, e.parent_ && lt(e.parent_));
}
function $(e) {
  e.copy_ || (e.copy_ = at(e.base_, e.scope_.immer_.useStrictShallowCopy_));
}
var rn = class {
  constructor(e) {
    this.autoFreeze_ = !0, this.useStrictShallowCopy_ = !1, this.produce = (t, n, r) => {
      if (typeof t == "function" && typeof n != "function") {
        const a = n;
        n = t;
        const o = this;
        return function(l = a, ...h) {
          return o.produce(l, (p) => n.call(this, p, ...h));
        };
      }
      typeof n != "function" && j(6), r !== void 0 && typeof r != "function" && j(7);
      let i;
      if (O(t)) {
        const a = xt(this), o = ct(t, void 0);
        let s = !0;
        try {
          i = n(o), s = !1;
        } finally {
          s ? ot(a) : st(a);
        }
        return St(a, r), It(i, a);
      } else if (!t || typeof t != "object") {
        if (i = n(t), i === void 0 && (i = t), i === Kt && (i = void 0), this.autoFreeze_ && ut(i, !0), r) {
          const a = [], o = [];
          R("Patches").generateReplacementPatches_(t, i, a, o), r(a, o);
        }
        return i;
      } else j(1, t);
    }, this.produceWithPatches = (t, n) => {
      if (typeof t == "function")
        return (o, ...s) => this.produceWithPatches(o, (l) => t(l, ...s));
      let r, i;
      return [this.produce(t, n, (o, s) => {
        r = o, i = s;
      }), r, i];
    }, typeof (e == null ? void 0 : e.autoFreeze) == "boolean" && this.setAutoFreeze(e.autoFreeze), typeof (e == null ? void 0 : e.useStrictShallowCopy) == "boolean" && this.setUseStrictShallowCopy(e.useStrictShallowCopy);
  }
  createDraft(e) {
    O(e) || j(8), A(e) && (e = an(e));
    const t = xt(this), n = ct(e, void 0);
    return n[P].isManual_ = !0, st(t), n;
  }
  finishDraft(e, t) {
    const n = e && e[P];
    (!n || !n.isManual_) && j(9);
    const {
      scope_: r
    } = n;
    return St(r, t), It(void 0, r);
  }
  /**
   * Pass true to automatically freeze all copies created by Immer.
   *
   * By default, auto-freezing is enabled.
   */
  setAutoFreeze(e) {
    this.autoFreeze_ = e;
  }
  /**
   * Pass true to enable strict shallow copy.
   *
   * By default, immer does not copy the object descriptors such as getter, setter and non-enumrable properties.
   */
  setUseStrictShallowCopy(e) {
    this.useStrictShallowCopy_ = e;
  }
  applyPatches(e, t) {
    let n;
    for (n = t.length - 1; n >= 0; n--) {
      const i = t[n];
      if (i.path.length === 0 && i.op === "replace") {
        e = i.value;
        break;
      }
    }
    n > -1 && (t = t.slice(n + 1));
    const r = R("Patches").applyPatches_;
    return A(e) ? r(e, t) : this.produce(e, (i) => r(i, t));
  }
};
function ct(e, t) {
  const n = Z(e) ? R("MapSet").proxyMap_(e, t) : q(e) ? R("MapSet").proxySet_(e, t) : en(e, t);
  return (t ? t.scope_ : Gt()).drafts_.push(n), n;
}
function an(e) {
  return A(e) || j(10, e), Zt(e);
}
function Zt(e) {
  if (!O(e) || Y(e)) return e;
  const t = e[P];
  let n;
  if (t) {
    if (!t.modified_) return t.base_;
    t.finalized_ = !0, n = at(e, t.scope_.immer_.useStrictShallowCopy_);
  } else
    n = at(e, !0);
  return K(n, (r, i) => {
    Bt(n, r, Zt(i));
  }), t && (t.finalized_ = !1), n;
}
var g = new rn(), on = g.produce;
g.produceWithPatches.bind(g);
g.setAutoFreeze.bind(g);
g.setUseStrictShallowCopy.bind(g);
g.applyPatches.bind(g);
g.createDraft.bind(g);
g.finishDraft.bind(g);
const Rt = {
  ar_EG: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./ar_EG-CGRlXlYm.js").then((t) => t.a), import("./ar-C-VdRq33.js").then((t) => t.a)]);
    return {
      antd: e,
      dayjs: "ar"
    };
  },
  az_AZ: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./az_AZ-WGBZTwT5.js").then((t) => t.a), import("./az-DAoIrAXO.js").then((t) => t.a)]);
    return {
      antd: e,
      dayjs: "az"
    };
  },
  bg_BG: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./bg_BG-GIJhoRVR.js").then((t) => t.b), import("./bg-yL6s-I7p.js").then((t) => t.b)]);
    return {
      antd: e,
      dayjs: "bg"
    };
  },
  bn_BD: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./bn_BD-BY-F4RT1.js").then((t) => t.b), import("./bn-CQZ-NIUs.js").then((t) => t.b)]);
    return {
      antd: e,
      dayjs: "bn"
    };
  },
  by_BY: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./by_BY-BO6LgLuY.js").then((t) => t.b),
      import("./be-UwU2M5c_.js").then((t) => t.b)
      // Belarusian (Belarus)
    ]);
    return {
      antd: e,
      dayjs: "be"
    };
  },
  ca_ES: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./ca_ES-BD9K_B9k.js").then((t) => t.c), import("./ca-C3_DPseO.js").then((t) => t.c)]);
    return {
      antd: e,
      dayjs: "ca"
    };
  },
  cs_CZ: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./cs_CZ-B386UN72.js").then((t) => t.c), import("./cs-B3sbOvGV.js").then((t) => t.c)]);
    return {
      antd: e,
      dayjs: "cs"
    };
  },
  da_DK: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./da_DK-DlaKPPCY.js").then((t) => t.d), import("./da-BKb6zgr9.js").then((t) => t.d)]);
    return {
      antd: e,
      dayjs: "da"
    };
  },
  de_DE: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./de_DE-C4AeO4LT.js").then((t) => t.d), import("./de-BFP3vWhR.js").then((t) => t.d)]);
    return {
      antd: e,
      dayjs: "de"
    };
  },
  el_GR: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./el_GR-DNwhfLlY.js").then((t) => t.e), import("./el-D70QUesW.js").then((t) => t.e)]);
    return {
      antd: e,
      dayjs: "el"
    };
  },
  en_GB: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./en_GB-DD7ELRaN.js").then((t) => t.e), import("./en-gb-DK3Yaqxy.js").then((t) => t.e)]);
    return {
      antd: e,
      dayjs: "en-gb"
    };
  },
  en_US: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./en_US-BSaAW192.js").then((t) => t.e), import("./en-7Td39058.js").then((t) => t.e)]);
    return {
      antd: e,
      dayjs: "en"
    };
  },
  es_ES: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./es_ES-BG-vjDXi.js").then((t) => t.e), import("./es-BT0gyjYk.js").then((t) => t.e)]);
    return {
      antd: e,
      dayjs: "es"
    };
  },
  et_EE: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./et_EE-CchTk3r-.js").then((t) => t.e), import("./et-C0-ZlJGj.js").then((t) => t.e)]);
    return {
      antd: e,
      dayjs: "et"
    };
  },
  eu_ES: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./eu_ES-DmdF8xdh.js").then((t) => t.e),
      import("./eu-D1RHx6e1.js").then((t) => t.e)
      // Basque
    ]);
    return {
      antd: e,
      dayjs: "eu"
    };
  },
  fa_IR: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./fa_IR-QaoumPC4.js").then((t) => t.f), import("./fa-C6szgq7X.js").then((t) => t.f)]);
    return {
      antd: e,
      dayjs: "fa"
    };
  },
  fi_FI: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./fi_FI-CNb7YJKh.js").then((t) => t.f), import("./fi-C6SbWD9n.js").then((t) => t.f)]);
    return {
      antd: e,
      dayjs: "fi"
    };
  },
  fr_BE: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./fr_BE-Cg-GnAXf.js").then((t) => t.f), import("./fr-D56FHfLQ.js").then((t) => t.f)]);
    return {
      antd: e,
      dayjs: "fr"
    };
  },
  fr_CA: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./fr_CA-DA82FUzC.js").then((t) => t.f), import("./fr-ca-DxQZWR4Z.js").then((t) => t.f)]);
    return {
      antd: e,
      dayjs: "fr-ca"
    };
  },
  fr_FR: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./fr_FR-DmsTQ0-z.js").then((t) => t.f), import("./fr-D56FHfLQ.js").then((t) => t.f)]);
    return {
      antd: e,
      dayjs: "fr"
    };
  },
  ga_IE: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./ga_IE-Dgpq4Lqg.js").then((t) => t.g),
      import("./ga-B8LQU9Ls.js").then((t) => t.g)
      // Irish
    ]);
    return {
      antd: e,
      dayjs: "ga"
    };
  },
  gl_ES: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./gl_ES-w-aH9KX0.js").then((t) => t.g),
      import("./gl-BXRQLU8R.js").then((t) => t.g)
      // Galician
    ]);
    return {
      antd: e,
      dayjs: "gl"
    };
  },
  he_IL: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./he_IL-QMrUYeOG.js").then((t) => t.h), import("./he-ClEQOVBx.js").then((t) => t.h)]);
    return {
      antd: e,
      dayjs: "he"
    };
  },
  hi_IN: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./hi_IN-13dnTT4u.js").then((t) => t.h), import("./hi-BeDF_XDO.js").then((t) => t.h)]);
    return {
      antd: e,
      dayjs: "hi"
    };
  },
  hr_HR: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./hr_HR-CKIlAQGO.js").then((t) => t.h), import("./hr-CaPMgs65.js").then((t) => t.h)]);
    return {
      antd: e,
      dayjs: "hr"
    };
  },
  hu_HU: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./hu_HU-OIJqZRMw.js").then((t) => t.h), import("./hu-VIt0WEP4.js").then((t) => t.h)]);
    return {
      antd: e,
      dayjs: "hu"
    };
  },
  hy_AM: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./hy_AM-Umkpp7C3.js").then((t) => t.h),
      import("./am-DdKAjlCj.js").then((t) => t.a)
      // Armenian
    ]);
    return {
      antd: e,
      dayjs: "am"
    };
  },
  id_ID: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./id_ID-BH1QqNmF.js").then((t) => t.i), import("./id-B_uM1cf_.js").then((t) => t.i)]);
    return {
      antd: e,
      dayjs: "id"
    };
  },
  is_IS: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./is_IS-CjrkhC0H.js").then((t) => t.i), import("./is-RNsFkdD9.js").then((t) => t.i)]);
    return {
      antd: e,
      dayjs: "is"
    };
  },
  it_IT: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./it_IT-Wo0i3pTZ.js").then((t) => t.i), import("./it-CE__-abB.js").then((t) => t.i)]);
    return {
      antd: e,
      dayjs: "it"
    };
  },
  ja_JP: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./ja_JP-D0fOJfC-.js").then((t) => t.j), import("./ja-CidN9lGY.js").then((t) => t.j)]);
    return {
      antd: e,
      dayjs: "ja"
    };
  },
  ka_GE: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./ka_GE-Cpeky-JP.js").then((t) => t.k),
      import("./ka-BqEjgYpO.js").then((t) => t.k)
      // Georgian
    ]);
    return {
      antd: e,
      dayjs: "ka"
    };
  },
  kk_KZ: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./kk_KZ-CAoncoZI.js").then((t) => t.k),
      import("./kk-B1kRlSZS.js").then((t) => t.k)
      // Kazakh
    ]);
    return {
      antd: e,
      dayjs: "kk"
    };
  },
  km_KH: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./km_KH-BMlNAx5T.js").then((t) => t.k),
      import("./km-CXPBQ-a3.js").then((t) => t.k)
      // Khmer
    ]);
    return {
      antd: e,
      dayjs: "km"
    };
  },
  kmr_IQ: async () => {
    const [e] = await Promise.all([
      import("./kmr_IQ-Bw81WaBV.js").then((t) => t.k)
      // Not available in Day.js, so no need to load a locale file.
    ]);
    return {
      antd: e.default,
      dayjs: ""
    };
  },
  kn_IN: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./kn_IN-DaF_LLX6.js").then((t) => t.k),
      import("./kn-BUDzm5ug.js").then((t) => t.k)
      // Kannada
    ]);
    return {
      antd: e,
      dayjs: "kn"
    };
  },
  ko_KR: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./ko_KR-ZSv0gtZ1.js").then((t) => t.k), import("./ko-BMpv3C-n.js").then((t) => t.k)]);
    return {
      antd: e,
      dayjs: "ko"
    };
  },
  ku_IQ: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./ku_IQ-CLAUbh-w.js").then((t) => t.k),
      import("./ku-DHZAIb7D.js").then((t) => t.k)
      // Kurdish (Central)
    ]);
    return {
      antd: e,
      dayjs: "ku"
    };
  },
  lt_LT: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./lt_LT-Da0gCeMr.js").then((t) => t.l), import("./lt-D5cc_etB.js").then((t) => t.l)]);
    return {
      antd: e,
      dayjs: "lt"
    };
  },
  lv_LV: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./lv_LV-B0XNK-I6.js").then((t) => t.l), import("./lv-B7NDBym1.js").then((t) => t.l)]);
    return {
      antd: e,
      dayjs: "lv"
    };
  },
  mk_MK: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./mk_MK-DF6NMjU3.js").then((t) => t.m),
      import("./mk-C2Oodj29.js").then((t) => t.m)
      // Macedonian
    ]);
    return {
      antd: e,
      dayjs: "mk"
    };
  },
  ml_IN: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./ml_IN-D5kjQLJV.js").then((t) => t.m),
      import("./ml-BDELoLVZ.js").then((t) => t.m)
      // Malayalam
    ]);
    return {
      antd: e,
      dayjs: "ml"
    };
  },
  mn_MN: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./mn_MN-o3j_dfkw.js").then((t) => t.m),
      import("./mn-Bv0XYXJX.js").then((t) => t.m)
      // Mongolian
    ]);
    return {
      antd: e,
      dayjs: "mn"
    };
  },
  ms_MY: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./ms_MY-CmFa8Bma.js").then((t) => t.m), import("./ms-D309m7rs.js").then((t) => t.m)]);
    return {
      antd: e,
      dayjs: "ms"
    };
  },
  my_MM: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./my_MM-DjMFJiIh.js").then((t) => t.m),
      import("./my-C1-QmHgo.js").then((t) => t.m)
      // Burmese
    ]);
    return {
      antd: e,
      dayjs: "my"
    };
  },
  nb_NO: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./nb_NO-C3AlWpJh.js").then((t) => t.n),
      import("./nb-Cg5ZUgyC.js").then((t) => t.n)
      // Norwegian Bokmål
    ]);
    return {
      antd: e,
      dayjs: "nb"
    };
  },
  ne_NP: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./ne_NP-DFOwEWRd.js").then((t) => t.n),
      import("./ne-DloiKesC.js").then((t) => t.n)
      // Nepali
    ]);
    return {
      antd: e,
      dayjs: "ne"
    };
  },
  nl_BE: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./nl_BE-B8S6PE64.js").then((t) => t.n),
      import("./nl-be-Bh4-ncqM.js").then((t) => t.n)
      // Dutch (Belgium)
    ]);
    return {
      antd: e,
      dayjs: "nl-be"
    };
  },
  nl_NL: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./nl_NL-B-nO_Wm2.js").then((t) => t.n),
      import("./nl-DbA1xAhh.js").then((t) => t.n)
      // Dutch (Netherlands)
    ]);
    return {
      antd: e,
      dayjs: "nl"
    };
  },
  pl_PL: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./pl_PL-DmQ1gG_M.js").then((t) => t.p), import("./pl-H3Btdiis.js").then((t) => t.p)]);
    return {
      antd: e,
      dayjs: "pl"
    };
  },
  pt_BR: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./pt_BR-BJ8GJ1lV.js").then((t) => t.p),
      import("./pt-br-Cyp3aieX.js").then((t) => t.p)
      // Portuguese (Brazil)
    ]);
    return {
      antd: e,
      dayjs: "pt-br"
    };
  },
  pt_PT: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./pt_PT-C0VbQazb.js").then((t) => t.p),
      import("./pt-GEgK_nk4.js").then((t) => t.p)
      // Portuguese (Portugal)
    ]);
    return {
      antd: e,
      dayjs: "pt"
    };
  },
  ro_RO: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./ro_RO-BNSUScdc.js").then((t) => t.r), import("./ro-sYBj_xSP.js").then((t) => t.r)]);
    return {
      antd: e,
      dayjs: "ro"
    };
  },
  ru_RU: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./ru_RU-C9bZn00-.js").then((t) => t.r), import("./ru-DvtoAmuM.js").then((t) => t.r)]);
    return {
      antd: e,
      dayjs: "ru"
    };
  },
  si_LK: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./si_LK-oaNnWiaR.js").then((t) => t.s),
      import("./si-CHuGNN1j.js").then((t) => t.s)
      // Sinhala
    ]);
    return {
      antd: e,
      dayjs: "si"
    };
  },
  sk_SK: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./sk_SK-DIzWoklN.js").then((t) => t.s), import("./sk-B2_uBu0i.js").then((t) => t.s)]);
    return {
      antd: e,
      dayjs: "sk"
    };
  },
  sl_SI: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./sl_SI-km6X_Zcu.js").then((t) => t.s), import("./sl-D-p6YTgy.js").then((t) => t.s)]);
    return {
      antd: e,
      dayjs: "sl"
    };
  },
  sr_RS: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./sr_RS-suIDjmIK.js").then((t) => t.s),
      import("./sr-Bvf0JNqQ.js").then((t) => t.s)
      // Serbian
    ]);
    return {
      antd: e,
      dayjs: "sr"
    };
  },
  sv_SE: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./sv_SE-CQM5xQ-H.js").then((t) => t.s), import("./sv-CbKzOxWk.js").then((t) => t.s)]);
    return {
      antd: e,
      dayjs: "sv"
    };
  },
  ta_IN: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./ta_IN-CxaCbHXu.js").then((t) => t.t),
      import("./ta-B2qHaLqm.js").then((t) => t.t)
      // Tamil
    ]);
    return {
      antd: e,
      dayjs: "ta"
    };
  },
  th_TH: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./th_TH-RfPLAKAV.js").then((t) => t.t), import("./th-Cfm25n4G.js").then((t) => t.t)]);
    return {
      antd: e,
      dayjs: "th"
    };
  },
  tk_TK: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./tk_TK-DUXm7xHt.js").then((t) => t.t),
      import("./tk-B9DHkvUy.js").then((t) => t.t)
      // Turkmen
    ]);
    return {
      antd: e,
      dayjs: "tk"
    };
  },
  tr_TR: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./tr_TR-C2L8D0eq.js").then((t) => t.t), import("./tr-BFzq-vu5.js").then((t) => t.t)]);
    return {
      antd: e,
      dayjs: "tr"
    };
  },
  uk_UA: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./uk_UA-BTlR5Yey.js").then((t) => t.u),
      import("./uk-CKzVl8OY.js").then((t) => t.u)
      // Ukrainian
    ]);
    return {
      antd: e,
      dayjs: "uk"
    };
  },
  ur_PK: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./ur_PK-B6J1LEMh.js").then((t) => t.u),
      import("./ur-BL7um2oN.js").then((t) => t.u)
      // Urdu
    ]);
    return {
      antd: e,
      dayjs: "ur"
    };
  },
  uz_UZ: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./uz_UZ-CaliKvJr.js").then((t) => t.u),
      import("./uz-c1-_JTsw.js").then((t) => t.u)
      // Uzbek
    ]);
    return {
      antd: e,
      dayjs: "uz"
    };
  },
  vi_VN: async () => {
    const [{
      default: e
    }] = await Promise.all([import("./vi_VN-BMXLNZaz.js").then((t) => t.v), import("./vi-B4i9bc0z.js").then((t) => t.v)]);
    return {
      antd: e,
      dayjs: "vi"
    };
  },
  zh_CN: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./zh_CN-CK55_kO5.js").then((t) => t.z),
      import("./zh-cn-C3H6SLTc.js").then((t) => t.z)
      // Chinese (Simplified)
    ]);
    return {
      antd: e,
      dayjs: "zh-cn"
    };
  },
  zh_HK: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./zh_HK-BQ4Wj0L0.js").then((t) => t.z),
      import("./zh-hk-CkAxnpC5.js").then((t) => t.z)
      // Chinese (Hong Kong)
    ]);
    return {
      antd: e,
      dayjs: "zh-hk"
    };
  },
  zh_TW: async () => {
    const [{
      default: e
    }] = await Promise.all([
      import("./zh_TW-D6BND7AS.js").then((t) => t.z),
      import("./zh-tw-BIAgMuEk.js").then((t) => t.z)
      // Chinese (Taiwan)
    ]);
    return {
      antd: e,
      dayjs: "zh-tw"
    };
  }
}, sn = (e, t) => on(e, (n) => {
  Object.keys(t).forEach((r) => {
    const i = r.split(".");
    let a = n;
    for (let o = 0; o < i.length - 1; o++) {
      const s = i[o];
      a[s] || (a[s] = {}), a = a[s];
    }
    a[i[i.length - 1]] = /* @__PURE__ */ I.jsx(Wt, {
      slot: t[r],
      clone: !0
    });
  });
}), cn = Ke(({
  slots: e,
  themeMode: t,
  id: n,
  className: r,
  style: i,
  locale: a = "en_US",
  getTargetContainer: o,
  getPopupContainer: s,
  renderEmpty: l,
  setSlotParams: h,
  children: p,
  component: c,
  ..._
}) => {
  var u;
  const [m, k] = zt(), d = {
    dark: t === "dark",
    ...((u = _.theme) == null ? void 0 : u.algorithm) || {}
  }, y = X(s), w = X(o), E = X(l);
  Tt(() => {
    a && Rt[a] && Rt[a]().then(({
      antd: b,
      dayjs: f
    }) => {
      k(b), re.locale(f);
    });
  }, [a]);
  const v = c || ne;
  return /* @__PURE__ */ I.jsx("div", {
    id: n,
    className: r,
    style: i,
    children: /* @__PURE__ */ I.jsx(ee, {
      hashPriority: "high",
      container: document.body,
      children: /* @__PURE__ */ I.jsx(v, {
        prefixCls: "ms-gr-ant",
        ...sn(_, e),
        locale: m,
        getPopupContainer: y,
        getTargetContainer: w,
        renderEmpty: e.renderEmpty ? Ye({
          slots: e,
          setSlotParams: h,
          key: "renderEmpty"
        }) : E,
        theme: {
          cssVar: !0,
          ..._.theme,
          algorithm: Object.keys(d).map((b) => {
            switch (b) {
              case "dark":
                return d[b] ? ht.darkAlgorithm : null;
              case "compact":
                return d[b] ? ht.compactAlgorithm : null;
              default:
                return null;
            }
          }).filter(Boolean)
        },
        children: p
      })
    })
  });
});
export {
  cn as ConfigProvider,
  cn as default
};
